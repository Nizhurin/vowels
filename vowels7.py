vowels = set('aeiou')

word = input("Provide a word to search for vowels: ")

found = sorted(list(vowels.intersection(set(word))))

for vowel in found:
    print(vowel)