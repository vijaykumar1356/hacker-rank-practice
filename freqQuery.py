#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(arr):
    d = defaultdict(int)
    cnt = defaultdict(int)
    new = []
    for i in arr:
        if i[0] == 1:
            cnt[d[i[1]]] -= 1
            d[i[1]] += 1
            cnt[d[i[1]]] += 1
        elif i[0] == 2:
            if d[i[1]]>0 :
                cnt[d[i[1]]] -= 1
                d[i[1]] -= 1
                cnt[d[i[1]]] += 1        
        else:
            new.append(1) if cnt[i[1]]>0 else new.append(0)
    return new

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print(*ans,sep="\n")
