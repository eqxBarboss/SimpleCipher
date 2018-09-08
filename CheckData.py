AlphRus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
Digits = '0123456789'


def CheckDigitsPositiveStr(s):

    tmp = ''
    if len(s):
        for i in s:
            tmp += i
            if Digits.find(i) == -1:
                return False
        if int(tmp):
            return True
    return False


def CheckRusStr(s):

    if len(s):
        for i in s:
            if AlphRus.find(i) == -1:
                return False
        return True
    return False


def CheckNothing(s):

    return True


def CheckFile(FileName, Mask):
    
    try:
        inputF = open(FileName)
        for line in inputF:
            for i in line:
                if Mask.find(i) != -1:
                    return True
    except FileNotFoundError:
        inputF = open(FileName, 'w')
        inputF.close()
        return False
    except Exception:
        return False