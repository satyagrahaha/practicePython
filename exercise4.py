number = int(input("Enter a number: "))
divisors = []
for i in range(1, number):
    if number % i == 0:
        divisors.append(i)
print(str(number) + " is divisible by " + str(divisors))
