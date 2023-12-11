def custom_map(function, iterable):
    for item in iterable:
        yield function(item)

def custom_zip(*iterables):
    iterators = tuple(map(iter, iterables))
    while True:
        t = tuple(map(next, iterators))
        if len(t) != len(iterators):
            break
        yield t

def custom_enumerate(iterable, start=0):
    for item in iterable:
        yield start, item
        start += 1

fruits = ['apple', 'banana', 'cherry']
enumerated = custom_enumerate(fruits, 1)
for index, fruit in enumerated:
    print(f"{index}: {fruit}")

a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = custom_zip(a, b)
for item in zipped:
    print(item)

def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared = custom_map(square, numbers)
for item in squared:
    print(item)