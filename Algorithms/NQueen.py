def feasible(queen, k):
    i = 0
    while i < k:
        if queen[k] == queen[i] or abs(queen[i] - queen[k]) == abs(i - k):
            return False
        i += 1
    return True

def nqueens(queen, k, size):
    if k == size:
        print(queen)
        return
    i = 0
    while i < size:
        queen[k] = i
        if feasible(queen, k):
            nqueens(queen, k + 1, size)
        i += 1

# Testing Code
queen = [0] * 8
nqueens(queen, 0, 8)

"""
[0, 4, 7, 5, 2, 6, 1, 3]
[0, 5, 7, 2, 6, 3, 1, 4]
[0, 6, 3, 5, 7, 1, 4, 2]
........
........
[7, 2, 0, 5, 1, 4, 6, 3]
[7, 3, 0, 2, 5, 1, 6, 4]
"""

