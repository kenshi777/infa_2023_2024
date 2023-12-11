import os
import string
import pickle
from typing import Iterable

class TextLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.index = 0
        self.refresh_file_list()

    def refresh_file_list(self):
        self.text_files = [file for file in os.listdir(self.folder_path)]

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

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['index']  # Exclude the index from serialization
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.index = 0
        self.refresh_file_list()  # Refresh the file list after deserialization

data_folder = "./sample/"
text_loader = TextLoader(data_folder)

print("Количество текстов в папке:", len(text_loader))

# Получение итерируемых текстов
for text in text_loader:
    print(text)

# Сериализация
with open('text_loader.pickle', 'wb') as f:
    pickle.dump(text_loader, f)

# Десериализация
with open('text_loader.pickle', 'rb') as f:
    deserialized_loader = pickle.load(f)

print("\nДесериализованный объект:")
for text in deserialized_loader:
    print(text)