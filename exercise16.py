import random
import re
import string

strength = ''

while strength != 'strong' and strength != 'weak':
    strength = input('select strong or weak: ')


def createPass(passStrength):
    if passStrength == 'weak':
        with open('/Users/hellerj/pythonStuff/words_alpha.txt', 'r') as f:
            word1 = random.choice(list(f))
            word1 = re.sub('\n', '', word1)
        with open('/Users/hellerj/pythonStuff/words_alpha.txt', 'r') as f:
            word2 = random.choice(list(f))
            word2 = re.sub('\n', '', word2)
        return word1 + word2.capitalize()

    elif passStrength == 'strong':
        return ''.join(random.choices(string.ascii_letters
                + string.punctuation, k=18))


password = createPass(strength)

print('Your new password is ' + password + '.')
