# this code is to print out total happiness after traversing in lists A, B
# 
n, m = map(int, input().split())
sample_array = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(sum([(i in a) - (i in b) for i in sample_array]))
