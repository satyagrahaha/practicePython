import random

def zeroPad(unpadded):
    for i in range(len(unpadded), 4):
        unpadded = '0' + unpadded
    return unpadded

secret = str(random.randint(0, 9999))
secret = zeroPad(secret)
guess = ''
trys = 0

#print(secret)

if __name__ == "__main__":
    
    print('Welcome to the Cows and Bulls Game!')


    while guess != secret:
        guess = input('Enter a number: ')
        guess = zeroPad(guess)
        trys += 1
        cows = 0
        bulls = 0

        for i in range(0, 4):
            if guess[i] == secret[i]:
                cows += 1

        guessSet = set(guess)

        for i in guessSet:
            if i in secret:
                bulls += 1

        print(str(cows) + ' cows, ' + str(bulls) + ' bulls')
        
        #print(str(secret) + str(guess))
      
    print('Congratulations! ' + str(trys) + ' guesses.')  


