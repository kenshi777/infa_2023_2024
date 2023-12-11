def swap(func):
    def wrapper(*args, **kwargs):
        reversed_args = args[::-1]
        return func(*reversed_args, **kwargs)
    return wrapper

@swap
def example(*args):
    return args

res = example(1, 2, 3)
print(res)