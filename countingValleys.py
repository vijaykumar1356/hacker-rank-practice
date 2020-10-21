def countingValleys(steps, path):
    level = 0
    vly = 0
    for i in path:
        if i == 'U':
            level += 1  
        else: 
            level -= 1
        if level==0 and i == 'U':
            vly += 1
    return vly


steps = int(input().strip())

path = input()

result = countingValleys(steps, path)
print(result)