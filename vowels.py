vowels = ['a', 'e', 'i', 'o', 'u']
word = "MilliwAys"

for letter in word:
    if letter.lower() in vowels:
        print(letter.lower())