class PrintCurrent(Exception):
    pass

class PrintSum(Exception):
    pass

class PrintMean(Exception):
    pass

class PrintVar(Exception):
    pass

def sum_coroutine():
    print("Starting coroutine")
    s = 0
    try:
        while True:
            try:
                x = yield
                s += x
            except PrintCurrent:
                yield x
            except PrintSum:
                yield s
    finally:
        print("Stop coroutine")

def mean_coroutine():
    print("Starting coroutine")
    s = 0
    n = 0
    m = 0
    try:
        while True:
            try:
                x = yield
                s += x
                n += 1
                m = s / n
            except PrintCurrent:
                yield x
            except PrintMean:
                yield m
    finally:
        print("Stop coroutine")

def var_coroutine():
    print("Starting coroutine")
    s1 = 0
    s2 = 0
    n = 0
    v = 0
    try:
        while True:
            try:
                x = yield
                s1 += x
                s2 += x ** 2
                n += 1
                v = (s2 / n - s1 ** 2 / n)
            except PrintCurrent:
                yield x
            except PrintVar:
                yield v
    finally:
        print("Stop coroutine")

coroutine_1 = mean_coroutine()
coroutine_2 = var_coroutine()
next(coroutine_1)
next(coroutine_2)
for i in range(1, 12):
    coroutine_1.send(i)
    coroutine_2.send(i)
    print("Current element:", coroutine_1.throw(PrintCurrent))
    print("Current element:", coroutine_2.throw(PrintCurrent))
    next(coroutine_1)
    next(coroutine_2)

print(coroutine_1.throw(PrintMean))
print(coroutine_2.throw(PrintVar))

coroutine_1.close()
coroutine_2.close()