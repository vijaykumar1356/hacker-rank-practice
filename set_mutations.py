# the following is a solution to set mutations problem from hackerrank
a = int(input())
set_a = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    j, k = input().split()
    new_set = set(map(int, input().split()))
    if j == "update":
        set_a.update(new_set)
    elif j == "intersection_update":
        set_a.intersection_update(new_set)
    elif j == "difference_update":
        set_a.difference_update(new_set)
    elif j == "symmetric_difference_update":
        set_a.symmetric_difference_update(new_set)
    else:
        pass
print(sum(set_a))

