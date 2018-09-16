import math
import FormatOutput


AlphRus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def GetFactors(val):
    res = []
    for i in range(2, val // 2 + 1):
        if val % i == 0:
            res.append(i)
    res.append(val)
    return res

def SortFactors(a):
    return a[1]

def KasiskiTest(InputFileName, OutputFileName):

    inF = open(InputFileName)
    s = inF.read()
    inF.close()

    s = s.strip()
    tmp = ''

    for i in range(len(s)):
        if AlphRus.find(s[i]) != -1:
            a = AlphRus.index(s[i]) 
            if a > 32:
                a -= 33 
            tmp += AlphRus[a]
    s = tmp

    substr = []
    repindex = []

    i = 0
    while i < len(s) - 6:
        j = i + 3
        while j < len(s) - 3:
            if s[i : i + 3] == s[j : j + 3]:
                if substr.count(s[i : i + 3]) == 0:
                    substr.append(s[i : i + 3])
                    repindex.append([])
                    repindex[-1].append(i)
                repindex[substr.index(s[j : j + 3])].append(j)
                break 
            j += 1
        i += 1

    distances = []
    for i in repindex:
        for j in range(len(i) - 1):
            if distances.count(i[j + 1] - i[j]) == 0:
                distances.append(i[j + 1] - i[j])

    factors = []
    countfactors = []
    for i in distances:
        currfactors = GetFactors(i)
        for j in currfactors:
            if factors.count(j):
                countfactors[factors.index(j)] += 1
            else:
                factors.append(j)
                countfactors.append(1)

    resarr = [[factors[i], countfactors[i]] for i in range(len(factors))]
    resarr.sort(key = SortFactors, reverse = 1)
 
    if len(resarr) > 30:
        resarr = resarr[: 30]

    StrFactors = "Factors |" + FormatOutput.TableStr([resarr[i][0] for i in range(len(resarr))], "|", 3)
    Sep = "_" * len(StrFactors)
    StrCount = "Count   |" + FormatOutput.TableStr([resarr[i][1] for i in range(len(resarr))], "|", 3) 

    outF = open(OutputFileName, 'wt')
    outF.write(StrFactors + "\n")
    outF.write(Sep + "\n")
    outF.write(StrCount + "\n")
    outF.close()
    
    return
