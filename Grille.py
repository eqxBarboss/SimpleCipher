AlphEng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

Grille = [[1, 0, 0, 0], 
          [0, 0, 0, 1],
          [0, 0, 1, 0], 
          [0, 1, 0, 0]]


def GetLinearGrille(Grille):

    key = len(Grille)
    RttngMatr = [[Grille[i][j] for j in range(key)] for i in range(key)]
    Matr = [[Grille[i][j] for j in range(key)] for i in range(key)]
    curr = 0

    for i in range(key):
        for j in range(key):
            if RttngMatr[i][j]:
                Matr[i][j] = curr
                curr += 1

    for _ in range(3):
        tmpMatr = [[RttngMatr[i][j] for j in range(key)] for i in range(key)]

        for i in range(key):
            for j in range(key):
                if tmpMatr[i][j]:
                    RttngMatr[i][j] = 0
                    RttngMatr[j][key - 1 - i] = 1

        for i in range(key):
            for j in range(key):
                if RttngMatr[i][j]:
                    Matr[i][j] = curr
                    curr += 1

    linearMatr = [Matr[i][j] for i in range(key) for j in range(key)]
    return linearMatr


def CipherGrille(InputFileName, OutputFileName, key):

    inF = open(InputFileName)
    s = inF.read()
    inF.close()

    s = s.strip()
    s = s.upper()
    key = len(Grille)
    tmp = ''
    spaceArr = []

    for i in range(len(s)):
        if AlphEng.find(s[i]) != -1:
            tmp += s[i]
        elif s[i] == ' ':
            spaceArr.append(len(tmp) + len(spaceArr))
    s = tmp

    delta = len(s) % (key * key)
    if delta:
        for i in range(key * key - delta):
            s += AlphEng[i]

    res = ''
    curr = 0
    overall = len(s) // (key * key)
    linearMatr = GetLinearGrille(Grille)

    while overall - curr:
        for _ in linearMatr:
            res += s[_ + curr * key * key]
            if len(spaceArr) and (len(res) == spaceArr[0]):
                res += ' '
                spaceArr = spaceArr[1 : len(spaceArr)]
        curr += 1

    outF = open(OutputFileName, 'wt')
    outF.write(res)
    outF.close()
    return


def EncipherGrille(InputFileName, OutputFileName, key):
    
    inF = open(InputFileName)
    s = inF.read()
    inF.close()

    key = 4
    s = s.strip()
    s = s.upper()
    tmp = ''
    spaceArr = []

    for i in range(len(s)):
        if AlphEng.find(s[i]) != -1:
            tmp += s[i]
        elif s[i] == ' ':
            spaceArr.append(len(tmp) + len(spaceArr))
    s = tmp

    delta = len(s) % (key * key)
    if delta:
        for i in range(key * key - delta):
            s += AlphEng[i]

    res = ''
    curr = 0
    overall = len(s) // (key * key)
    linearMatr = GetLinearGrille(Grille)

    while overall - curr:
        for _ in range(key * key):
            res += s[linearMatr.index(_) + curr * key * key]
            if len(spaceArr) and (len(res) == spaceArr[0]):
                res += ' '
                spaceArr = spaceArr[1 : len(spaceArr)]
        curr += 1

    outF = open(OutputFileName, 'wt')
    outF.write(res)
    outF.close()
    return