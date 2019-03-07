def decode(text):
    i = 0
    value = 0
    n = len(text)
    output = ""
    stk = []
    while i < n :
        if text[i].isdigit() :
            value = value*10 + int(text[i])
        elif text[i] == '[':
            stk.append(value)
            value = 0
            stk.append('[')
        elif text[i] == ']' :
            st = ""
            temp = stk.pop()
            while temp != '[' :
                st = temp + st
                temp = stk.pop()

            count = stk.pop()
            st2 = ""
            for _ in range(count):
                st2 += st
            stk.append(st2)
        else :
            stk.append(text[i])
        i += 1

    while len(stk) != 0:
        output = stk.pop() + output
    return output
#str = '3[Z]'
str = '1[x4[y]]13[Z]1[a]'
print(decode(str))