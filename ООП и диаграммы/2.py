class Mother:
    def __str__(self):
        return "Это материнский класс"
    
class Daughter(Mother):
    def __str__(self):
        return "Это дочерний класс"
    
mother = Mother()
daughter = Daughter()

print(mother)
print(daughter)