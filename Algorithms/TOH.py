def toh_util(num, source, dest, temp):
    if num < 1:
        return
    toh_util(num - 1, source, temp, dest)
    print("Move disk", num, "from peg", source, "to peg", dest)
    toh_util(num - 1, temp, dest, source)

def tower_of_hanoi(num):
    print("The sequence of moves involved in the Tower of Hanoi are:")
    toh_util(num, 'A', 'C', 'B')

# Testing Code
tower_of_hanoi(3)

"""
The sequence of moves involved in the Tower of Hanoi are :
Move disk 1 from peg A to peg C
Move disk 2 from peg A to peg B
Move disk 1 from peg C to peg B
Move disk 3 from peg A to peg C
Move disk 1 from peg B to peg A
Move disk 2 from peg B to peg C
Move disk 1 from peg A to peg C
"""