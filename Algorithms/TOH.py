def TOHUtil(num, source, dest, temp):
    if num < 1:
        return
    TOHUtil(num - 1, source, temp, dest)
    print(("Move disk" , num , "from peg" , source , "to peg" , dest))
    TOHUtil(num - 1, temp, dest, source)

def TowersOfHanoi(num):
    print("The sequence of moves involved in the Tower of Hanoi are :")
    TOHUtil(num, 'A', 'C', 'B')

TowersOfHanoi(3)
