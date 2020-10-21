n, m = map(int, input().split())
athletes = []
for _ in range(n):
    athletes.append(list(map(int, input().split())))
k = int(input())
for i in (sorted(athletes, key=lambda athlete: athlete[k])):
    print(*i)
