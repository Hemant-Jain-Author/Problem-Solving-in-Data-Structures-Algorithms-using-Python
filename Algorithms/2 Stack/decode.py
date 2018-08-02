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
            if output != "" :
                stk.append(output)
                output = ""
            stk.append(value)
            value = 0
            stk.append('[')
        elif text[i] == ']' :
            temp = stk.pop()
            while temp != '[' :
                temp += stk.pop()
            count = stk.pop()
            output = ""
            for _ in range(count):
                output += temp
        else :
            output = output + text[i]
        i += 1
    while len(stk) != 0:
        output = stk.pop() + output
    return output
str = '3[Z]'
# str = '1[x4[y]]13[Z]1[a]'
print(decode(str))