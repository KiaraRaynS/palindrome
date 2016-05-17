word = input('What word do you want to check? ')
word_inverse = word[::-1]

if word == word_inverse:
    print('That is indeed a palindrome')
else:
    print('That word is not a palindrome.')