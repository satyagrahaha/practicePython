firstNumber = int(input('Enter first number: '))
secondNumber = int(input('Enter second number: '))
if firstNumber % secondNumber == 0:
    print(str(firstNumber) + ' is divisible by ' + str(secondNumber) + '.')
else:
    print(str(firstNumber) + ' is not divisible by ' + str(secondNumber) + '.')
#if number % 2 == 0:
#    if number % 4 ==0:
#        print( str(number) + ' is divisible by four.')
#    else:
#        print( str(number) + ' is even.')
#elif number % 2 !=0:
#    print( str(number) + ' is odd.')
