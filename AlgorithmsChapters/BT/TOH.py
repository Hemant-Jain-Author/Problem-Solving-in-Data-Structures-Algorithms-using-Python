def toh_util(num,  src,  dst,  temp) :
    if (num < 1) :
        return
    toh_util(num - 1, src, temp, dst)
    print("Move disk " + str(num) + " src peg " + str(src) + " to peg " + str(dst))
    toh_util(num - 1, temp, dst, src)

def toh(num) :
    print("The sequence of moves involved in the Tower of Hanoi are :")
    toh_util(num, 'A', 'C', 'B')

# Testing Code
toh(3)


"""
sequence of moves involved in the Tower of Hanoi are :
Move disk 1 src peg A to peg C
Move disk 2 src peg A to peg B
Move disk 1 src peg C to peg B
Move disk 3 src peg A to peg C
Move disk 1 src peg B to peg A
Move disk 2 src peg B to peg C
Move disk 1 src peg A to peg C
"""
