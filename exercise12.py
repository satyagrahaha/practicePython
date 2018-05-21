a = [5, 10, 15, 20, 25]

def firstLast(fullList):
    firstLastList = fullList[0:len(fullList):len(fullList)-1]
    return firstLastList

print(firstLast(a))
