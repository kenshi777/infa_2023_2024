def bubble_sort(A):
    N = len(A)
    for i in range(1, N):
        for j in range(0, N-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

l = [5, 4, 3, 2, 1]

print(bubble_sort(l))

