import os
import string
from typing import Iterable

class TextLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.text_files = [file for file in os.listdir(folder_path)]
        self.index = 0

    def __len__(self):
        return len(self.text_files)

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index >= len(self):
                raise IndexError("Index out of range")
            filename = os.path.join(self.folder_path, self.text_files[index])
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
            return self._preprocess_text(text)
        elif isinstance(index, Iterable):
            return [self.__getitem__(i) for i in index]
        else:
            raise TypeError("Index must be an integer or iterable of integers")

    def _preprocess_text(self, text):
        text = text.lower()
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)
        return text

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self):
            text = self.__getitem__(self.index)
            self.index += 1
            return text
        else:
            self.index = 0
            raise StopIteration


data_folder = "./8/sample/"
text_loader = TextLoader(data_folder)

print("Количество текстов в папке:", len(text_loader))

# Получение итерируемых текстов
for text in text_loader:
    print(text)
