import pickle

# Пример сериализации итератора (список)
iterator_data = iter([1, 2, 3, 4, 5])

with open('iterator.pickle', 'wb') as f:
    pickle.dump(iterator_data, f)

with open('iterator.pickle', 'rb') as f:
    deserialized_iterator = pickle.load(f)

# Пример использования десериализованного итератора
for item in deserialized_iterator:
    print(item)


# Пример определения класса
class MyClass:
    def __init__(self, value):
        self.value = value

# Пример создания объекта и его сериализации
obj = MyClass(42)

with open('custom_class.pickle', 'wb') as f:
    pickle.dump(obj, f)

# Пример десериализации объекта
with open('custom_class.pickle', 'rb') as f:
    deserialized_obj = pickle.load(f)

# Пример использования десериализованного объекта
print(deserialized_obj.value)


from collections import deque

# Пример сериализации объекта из стандартной библиотеки
deque_data = deque([1, 2, 3, 4, 5])

with open('deque.pickle', 'wb') as f:
    pickle.dump(deque_data, f)

# Пример десериализации объекта из стандартной библиотеки
with open('deque.pickle', 'rb') as f:
    deserialized_deque = pickle.load(f)

# Пример использования десериализованного объекта
print(deserialized_deque)
