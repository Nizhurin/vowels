vowels = ['a', 'e', 'i', 'o', 'u']
found = []

word = "MilliwAys"

for letter in word:
    if letter.lower() in vowels:
        if letter.lower() not in found:
            found.append(letter.lower())
for vowel in found:
    print(vowel)