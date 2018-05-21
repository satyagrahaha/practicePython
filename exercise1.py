name = input('Enter your name: ')
age = input('Enter your age: ')
number = input('Enter a number: ')
year = 2018 + 100 - int(age)
for x in range(0, int(number)):
    print(name + ' you will turn 100 in ' + str(year) + '.')
