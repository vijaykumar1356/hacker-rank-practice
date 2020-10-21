# this is a solution to hacker rank problem on set operations
a = set(map(int, input().split()))
print(all([a.issuperset(set(map(int, input().split()))) for _ in range(int(input()))]))