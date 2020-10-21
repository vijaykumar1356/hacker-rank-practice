import numpy as np
# np.set_printoptions(legacy='1.13')
a, b = (np.array(input().split(), dtype=int) for _ in range(2))
print(np.inner(a, b), np.outer(a, b), sep="\n")