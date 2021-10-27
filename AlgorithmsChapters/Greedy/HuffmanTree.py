import heapq

class HuffmanTree :
    class Node  :
        def __init__(self, ch,  fr,  l,  r) :
            self.c = ch
            self.freq = fr
            self.left = l
            self.right = r

        def __lt__(self, other):
            return (self.freq < other.freq)

    def __init__(self, arr,  freq) :
        n = len(arr)
        hp =  []
        
        for i in range(n) :
            heapq.heappush(hp, self.Node(arr[i], freq[i], None, None))

        while (len(hp) > 1) :
            lt = heapq.heappop(hp)
            rt = heapq.heappop(hp)
            heapq.heappush(hp, self.Node('+', lt.freq + rt.freq, lt, rt))

        self.root = hp[0]

    def printUtil(self, root,  s) :
        if (root.left == None and root.right == None and root.c != '+') :
            print(str(root.c) + " = " + s)
            return
        self.printUtil(root.left, s + "0")
        self.printUtil(root.right, s + "1")

    def print(self) :
        print("Char = Huffman code")
        self.printUtil(self.root, "")

ar = ['A', 'B', 'C', 'D', 'E']
fr = [30, 25, 21, 14, 10]
hf = HuffmanTree(ar, fr)
hf.print()

"""
Char = Huffman code
C = 00
E = 010
D = 011
B = 10
A = 11
"""