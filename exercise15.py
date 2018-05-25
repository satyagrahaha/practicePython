longString = input("Enter a long string with spaces: ")

def backwards(forwardString):
    forwardWords = forwardString.split()
    backwardsWords = []
    for i in range((len(forwardWords) -1), -1, -1):
        backwardsWords.append(forwardWords[i])
    return ' '.join(backwardsWords)

print(backwards(longString))
        
