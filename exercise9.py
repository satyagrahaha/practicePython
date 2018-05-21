import random

secret = random.randrange(1, 9)
guess = 0

while guess != secret:
    guess = input('Guess or Exit: ')
    if int(guess) == secret:
        break
    if str(guess) == 'Exit':
        break
    if int(guess) < secret:
        print('Higher!')
    if int(guess) > secret:
        print('Lower!')

if guess == secret:
    print('You guessed the secret number, ' + str(secret))
else:
    print('Exiting...')
