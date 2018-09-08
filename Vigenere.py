AlphRus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def GetLetter(ch, delta):

    if delta < 0:
        delta += 33
    delta %= 33
    indexCh = AlphRus.index(ch)
    index = indexCh + delta
    if indexCh > 32:
        if index > 65:
            index -= 33
    else:
        if index > 32:
            index -= 33
    return AlphRus[index]
        

def CipherVigenere(InputFileName, OutputFileName, key):

    inF = open(InputFileName)
    s = inF.read()
    inF.close()

    s = s.strip()
    tmp = ''
    spaceArr = []

    for i in range(len(s)):
        if AlphRus.find(s[i]) != -1:
            tmp += s[i]
        elif s[i] == ' ':
            spaceArr.append(len(tmp) + len(spaceArr))
    s = tmp

    res = ''

    for i in range(len(s)):
        if i and (i % len(key)) == 0:
            tmp = key
            key = ''
            for j in tmp:
                key += GetLetter(j, 1)

        res += GetLetter(s[i], AlphRus.index(key[i % len(key)]) % 33)

        if len(spaceArr) and (len(res) == spaceArr[0]):
            res += ' '
            spaceArr = spaceArr[1 : len(spaceArr)]

    outF = open(OutputFileName, 'wt')
    outF.write(res)
    outF.close()
    return


def EncipherVigenere(InputFileName, OutputFileName, key):
    
    inF = open(InputFileName)
    s = inF.read()
    inF.close()

    s = s.strip()
    tmp = ''
    spaceArr = []

    for i in range(len(s)):
        if AlphRus.find(s[i]) != -1:
            tmp += s[i]
        elif s[i] == ' ':
            spaceArr.append(len(tmp) + len(spaceArr))
    s = tmp

    res = ''

    for i in range(len(s)):
        if i and (i % len(key)) == 0:
            tmp = key
            key = ''
            for j in tmp:
                key += GetLetter(j, 1)

        res += GetLetter(s[i], -(AlphRus.index(key[i % len(key)]) % 33))

        if len(spaceArr) and (len(res) == spaceArr[0]):
            res += ' '
            spaceArr = spaceArr[1 : len(spaceArr)]

    outF = open(OutputFileName, 'wt')
    outF.write(res)
    outF.close()
    return