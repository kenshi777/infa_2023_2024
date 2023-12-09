l = []
while True:
    n = input()
    if n == 'End':
        break
    l.append(int(n))

def search_min(A : list):
    m = A[0]
    for i in A:
        if i < m:
            m = i
    return m

def search_max(A : list):
    m = A[0]
    for i in A:
        if i > m:
            m = i
    return m

def mean(A : list):
    m = 0
    for i in A:
        m += i
    return m / len(A)

def disp(A : list):
    m = mean(A)
    r = 0
    for i in A:
        r += (m - i)**2
    return (r / (len(A)-1)) ** 0.5

print(search_min(l))
print(search_max(l))
print(mean(l))
print(disp(l))
