rps = ['rock', 'paper', 'scissors']

while True:
    player1 = input("Player 1, choose rock, paper, scissors: ")
    if player1 in rps:
        break

while True:
    player2 = input("Player 2, choose rock, paper, scissors: ")
    if player2 in rps:
        break

if player1 == 'rock':
    if player2 == 'rock':
        print("It's a tie!")
    if player2 == 'paper':
        print('Player 2 wins!')
    if player2 == 'scissors':
        print('Player 1 wins!')

if player1 == 'paper':
    if player2 == 'paper':
        print("It's a tie!")
    if player2 == 'scissors':
        print('Player 2 wins!')
    if player2 == 'rock':
        print('Player 1 wins!')


if player1 == 'scissors':
    if player2 == 'scissors':
        print("It's a tie!")
    if player2 == 'rock':
        print('Player 2 wins!')
    if player2 == 'paper':
        print('Player 1 wins!')
