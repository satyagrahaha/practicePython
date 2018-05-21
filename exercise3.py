fullList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
compare = int(input('Enter a number: '))
shortList = []
for element in fullList:
    if element < compare:
        shortList.append(element)
print(shortList)
