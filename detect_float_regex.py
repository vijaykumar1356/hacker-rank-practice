# detecting a floating point number in Hacker Rank
import re
test_result=[]
pattern = re.compile(r'^[+|-]?\d*\.[0-9]+$')
for _ in range(int(input())):
    test_result.append(bool(pattern.match(input())))
print(*test_result, sep="\n")