def sort_str(string):
    st = sorted(string)
    result1 = ''
    result2 = 0
    for i in st:
        if i.isalpha():
            result1 +=i
        else:
            result2 += int(i)
    sorted(result1)
    return result1+str(result2)