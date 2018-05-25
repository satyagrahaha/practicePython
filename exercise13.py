fib = [1, 1]

count = int(input('How many Fibonnaci numbers do you want: '))

print(count)

for i in range(1, count):
    fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])

print(fib)