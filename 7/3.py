from itertools import product, permutations, combinations, combinations_with_replacement, groupby

def get_cartesian_product(a, b):
    return list(product(a, b))

result = get_cartesian_product([1, 2], [3, 4])
print(result)

def get_permutations(s, n):
    result = [''.join(p) for p in permutations(s, n)]
    result.sort()
    print(result)

get_permutations("cat", 2)

def get_combinations(s, n):
    result = []
    for k in range(1, n + 1):
        for combo in combinations(s, k):
            result.append(''.join(combo))
    print(result)

get_combinations("cat", 2)


def get_combinations_with_r(s, n):
    result = list(combinations_with_replacement(s, n))
    result = [''.join(item) for item in result]
    print(result)

get_combinations_with_r("cat", 2)

def compress_string(s):
    compressed = [(len(list(group)), int(key)) for key, group in groupby(s)]
    print(compressed)

compress_string('1222311')


def maximize(lists, m):
    max_result = 0
    for combo in product(*lists):
        result = sum(x**2 for x in combo) % m
        max_result = max(max_result, result)
    print(max_result)

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
maximize(lists, m=1000)
