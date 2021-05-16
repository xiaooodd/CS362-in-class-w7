def w_count(string):
    str1 = str.strip(string)
    n = 1
    i = 0
    while i < len(str1):
        while str1[i] == ' ':
            n += 1
            i += 1
            break
        while str1[i] == ' ':
            i += 1
        i += 1
    return n