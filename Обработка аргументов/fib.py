import sys

def fibonacci(n):
    fib_sequence = [0, 1]

    if n <= 0:
        return []

    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence[-1]



print(fibonacci(int(sys.argv[-1])))