number = int(input('Enter a number: '))

divisors = []

for i in range(1, number):
    if number % i == 0:
        divisors.append(i)
if len(divisors) > 1:
    print(str(number) + ' is not prime, divisible by ' + str(divisors) + '.')
else:
    print(str(number) + ' is prime.')
