def decorator(func):
    def the_wrapper(N):
        k = func(N)
        if k == 0:
            return 'Нет('
        elif k > 10:
            return 'Очень много'
        else:
            return k
    return the_wrapper

@decorator
def count_even(N):
    c = 0
    for i in N:
        if i % 2 == 0:
            c += 1
    return c

print(count_even([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,2]))