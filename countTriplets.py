from collections import Counter
def countTriplets(arr, r):
	a = Counter(arr)
	b = Counter()
	print(b)
	s=0
	for i in arr:
		j = i//r
		k = i*r
		a[i] -= 1
		if b[j] and a[k] and not i%r:
			s += b[j]*a[k]
		b[i] += 1	
	return s

n,r = map(int,input().split())
arr = list(map(int,input().split()))
result = countTriplets(arr, r)