import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#a = []
#b = []
#for i in range(0, random.randrange(8, 40)):
#  if random.randrange(0, 9999) % 2 == 0:
#    a.append(random.randrange(1, 100))
#  else:
#    b.append(random.randrange(1, 100))

c = []

#for element in a:
#  if (element in b) and not(element in c):
#    c.append(element)

c = [element for element in a if (element in b) and ((element not in a[0:a.index(element)-1]) or (a.index(element) == 0))] 
print(c)
