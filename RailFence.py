AlphEng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def EncipherRailFence(InputFileName, OutputFileName, key):

    inF = open(InputFileName)
    s = inF.read()
    inF.close()

    key = int(key)
    s = s.strip()
    s = s.upper()
    tmp = ""
    spaceArr = []

    for i in range(len(s)):
        if AlphEng.find(s[i]) != -1:
            tmp += s[i]
        elif s[i] == ' ':
            spaceArr.append(len(tmp) + len(spaceArr))
    s = tmp

    res = ""

    if (key >= len(s)) or (key == 1):
        res = s
    else:
        for i in range(key):
            curr = i
            while curr < len(s):
                res += s[curr]
                if len(spaceArr) and (len(res) == spaceArr[0]):
                    res += ' '
                    spaceArr = spaceArr[1 : len(spaceArr)]
                curr += 2 * ((key - 1) * (curr // (key - 1) + 1) - curr)

    outF = open(OutputFileName, 'wt')
    outF.write(res)
    outF.close()
    return


def DecipherRailFence(InputFileName, OutputFileName, key):
    
    inF = open(InputFileName)
    s = inF.read()
    inF.close()

    key = int(key)
    s = s.strip()
    s = s.upper()
    tmp = ""
    spaceArr = []

    for i in range(len(s)):
        if AlphEng.find(s[i]) != -1:
            tmp += s[i]
        elif s[i] == ' ':
            spaceArr.append(len(tmp) + len(spaceArr))
    s = tmp

    res = ""

    if (key >= len(s)) or (key == 1):
        res = s
    else:
        rowLen = []

        for i in range(key):
            currLen = 0
            curr = i
            while curr < len(s):
                currLen += 1
                curr += 2 * ((key - 1) * (curr // (key - 1) + 1) - curr)
            rowLen.append(currLen)

        rowIndex = [0]

        for i in range(1, len(rowLen)):
            rowIndex.append(rowIndex[i - 1] + rowLen[i - 1])

        done = 0
        while len(s) - done:
            for j in range(len(rowIndex)):
                if len(s) - done: 
                    res += s[rowIndex[j]]
                    if len(spaceArr) and (len(res) == spaceArr[0]):
                        res += ' '
                        spaceArr = spaceArr[1 : len(spaceArr)]
                    rowIndex[j] += 1
                    done += 1
            for j in reversed(range(len(rowIndex))):
                if j and (j != len(rowIndex) - 1) and (len(s) - done):
                    res += s[rowIndex[j]]
                    if len(spaceArr) and (len(res) == spaceArr[0]):
                        res += ' '
                        spaceArr = spaceArr[1 : len(spaceArr)]
                    rowIndex[j] += 1
                    done += 1

    outF = open(OutputFileName, 'wt')
    outF.write(res)
    outF.close()
    return