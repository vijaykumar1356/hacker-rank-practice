
def hourglassSum(arr):
    x = []
    for i in arr:
        for j in range(len(i)-2):
            x.append(i[j]+i[j+1]+i[j+2])
    y = []
    for i in arr[1:-1]:
        for j in i[1:-1]:
            y.append(j)
    z = [sum(i) for i in list(zip(x[:16], y, x[8:]))]
    return max(z)



arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)
print(result)