def wild_char_match(exp,  str) :
    return  wild_char_match_util(exp, str, 0, 0)

def wild_char_match_util(exp,  str,  m,  n) :
    if (m == len(exp) and (n == len(str) or exp[m - 1] == '*')) :
        return  True

    if ((m == len(exp) and n != len(str)) or (m != len(exp) and n == len(str))) :
        return  False

    if (exp[m] == '?' or exp[m] == str[n]) :
        return  wild_char_match_util(exp, str, m + 1, n + 1)

    if (exp[m] == '*') :
        return  wild_char_match_util(exp, str, m + 1, n) or wild_char_match_util(exp, str, m, n + 1)

    return  False

def wild_char_match_dp(exp,  str) :
    return  wild_char_match_dp_util(exp, str, len(exp), len(str))

def wild_char_match_dp_util(exp,  str,  m,  n) :
    lookup = [[False] * (n + 1) for _ in range(m + 1)]
    lookup[0][0] = True
    #  empty exp and empty str match.
    #  0 row will remain all false. empty exp can't match any str.
    #  '*' can match with empty string, column 0 update.
    for i in range(1, m+1) :
        if (exp[i - 1] == '*') : 
            lookup[i][0] = lookup[i - 1][0]
        else :
            break

    #  Fill the table in bottom-up fashion
    for i in range(1, m+1) :
        for j in range(1, n+1) :
            #  If we see a '*' in pattern:
            #  1) We ignore '*' character and consider next character in the pattern.
            #  2) We ignore one character in the input str and consider next character.
            if (exp[i - 1] == '*') :
                lookup[i][j] = lookup[i - 1][j] or lookup[i][j - 1]
            elif (exp[i - 1] == '?' or str[j - 1] == exp[i - 1]) :
                lookup[i][j] = lookup[i - 1][j - 1]
            else :
                lookup[i][j] = False
    return  lookup[m][n]

print(wild_char_match("*llo,?World?", "Hello, World!"))
print(wild_char_match_dp("*llo,?World?", "Hello, World!"))

"""
True
True
"""