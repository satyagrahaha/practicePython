string = input("Enter a word: ")
isPalindrome = True
left = 0
right = len(string) - 1

while left != right:
    if string[left] == string[right]:
        left += 1
        right -= 1
    else:
        isPalindrome = False
        break

if isPalindrome:
    print(string + " is a palindrome.")
else:
    print(string + " is not a palindrome.")
        
