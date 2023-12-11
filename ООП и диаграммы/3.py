class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f'Я животное. Мое имя {self.name}, мой возраст {self.age}'
    
class Zebra(Animal):
    def __str__(self) -> str:
        return f'Я зебра. Мое имя {self.name}, мой возраст {self.age}'
    
class Dolphin(Animal):
    def __str__(self) -> str:
        return f'Я дельфин. Мое имя {self.name}, мой возраст {self.age}'
    
zebra = Zebra('Марти', 10)
dolphin = Dolphin('Олег', 52)

print(zebra)
print(dolphin)