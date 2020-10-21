n = int(input())
l = list(map(int, input().split()))
m = [str(i) == str(i)[::-1] for i in l]
print(all([i>0 for i in l]) and any(m))