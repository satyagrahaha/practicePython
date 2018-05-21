import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = []
b = []
for i in range(0, random.randrange(8, 40)):
    if random.randrange(0, 9999) % 2 == 0:
        a.append(random.randrange(1, 100))
    else:
        b.append(random.randrange(1, 100))
for element in a:
    if (element in b):
        print(str(element))
