from collections import Counter

seq = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
ctr = Counter(seq)
print(ctr)
print(ctr.get(3))
print(4 in ctr)
ctr.pop(4)
print(ctr)
print(4 in ctr)
ctr[5] += 1
ctr[3] -= 1
print(ctr)
