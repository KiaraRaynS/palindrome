import string
word = input('What would would you like checked? ').lower()
word = word.replace(" ", "")

for c in string.punctuation:
    word = word.replace(c,'')

count_1 = 0
count_2 = -1
a = word[count_1]
b = word[count_2]

for letter in word:
    if count_1 + 1 == len(word):
        print('That word appears to be a palindrome.')
        break
    elif a == b:
        count_1 += 1
        count_2 -= 1
        a = word[count_1]
        b = word[count_2]

    else:
        print('This word is not a palindrome.')
        break
