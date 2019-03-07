
class Stack(object):
    def __init__(self):
        self.data = []     

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return (len(self.data) == 0)

    def push(self, value):
        self.data.append(value)

    def top(self):
        if self.isEmpty():
            raise RuntimeError("StackEmptyException")
        return self.data[len(self.data) - 1]

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("StackEmptyException")
        return self.data.pop()


def printNumberPattern(expr):
    size = len(expr)
    output = [-1]*(size+1)
    val = 1
    count = 0

    for i in range(size) :
        curr = expr[i]
        if curr == 'D':
            count += 1
        elif curr == 'I':
            if count == 0:
                output[i] = val
                val += 1
                continue
            j = 0
            while j <= count :
                output[i - j] = val
                val += 1
                j += 1
            count = 0

    i = size
    j = 0
    while j <= count :
        output[i - j] = val
        val += 1
        j +=  1
    
    print(output)

printNumberPattern("DIDD")
printNumberPattern("DDIDDIID")
