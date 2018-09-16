def TableStr(arr, separator, signs):
    res = ""
    for i in arr:
        res += (signs - len(str(i))) * ' ' + str(i) + separator
    return res
