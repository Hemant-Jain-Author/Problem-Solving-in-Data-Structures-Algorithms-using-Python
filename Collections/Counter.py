from collections import Counter

seq = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
mycounter = Counter(seq)
print mycounter
print mycounter.get(3)
print mycounter.has_key(3)
mycounter.pop(4)
print mycounter
print 4 in mycounter
mycounter[5] += 1
mycounter[5] += 1
print mycounter
