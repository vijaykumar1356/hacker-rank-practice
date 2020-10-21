cube = lambda x: x*x*x# complete the lambda function 

def fibonacci(i):
    # return a list of fibonacci numbers
    l = [int]*i
    for j in range(i):
        if j == 0:
            l[j] = 0
        elif j == 1:
            l[j] = 1
        else:
            l[j] = l[j-1] + l[j-2]
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))