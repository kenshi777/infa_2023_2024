def print_coroutine():
    x = "start"
    s = 0
    l = []
    m = 0
    d = 0
    while True:
        x = yield x
        if x.isdigit():
            x = int(x)
            s += x
            l.append(x)
            count = len(l)
            m = s / count
            d = s ** 2 / count - m ** 2
            print("Got value", x)
        else:
            if x == 'mean':
                print('mean', m)
            elif x == 'var':
                print('var', d)
            elif x == 'count':
                print('count', count)
        

coroutine = print_coroutine()
print(next(coroutine))
while True:
    n = input()
    print(coroutine.send(n))