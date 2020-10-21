import collections


def circularRotate(n_list, k, queries):
    items = collections.deque(n_list)
    items.rotate(k)
    result = []
    for i in queries:
        result.append(n_list[i])
    return result
    


n, k, q = map(int, input().split())
n_list = list(map(int, input().split()))
queries = [int(input()) for _ in range(q)]
result = circularRotate(n_list, k, queries)
print("\n".join(map(str, result)))

