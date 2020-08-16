# this problem is to get 3 most common words from a given string
# hacker rank problem
from collections import Counter
d = Counter(sorted(input())).most_common()[:3]
for key, value in d:
    print(key, value)
