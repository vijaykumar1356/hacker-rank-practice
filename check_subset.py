# this code is the solution for hackerrank problem on subsets
result = []
for _ in range(int(input())):
    a = int(input())
    set_a = set(map(int, input().split()))
    b = int(input())
    set_b = set(map(int, input().split()))
    result.append(set_a.issubset(set_b))
print("\n".join(result))
