vowels = ['a', 'e', 'i', 'o', 'u']
found = {}

word = input("Provide a text to search for vowels: ")

for letter in word:
    if letter.lower() in vowels:
        found.setdefault(letter.lower(), 0)
        found[letter.lower()] += 1
print("Vowels - Count vowels in input text ")
for key,value in sorted(found.items()):
    print("Vowels",key,"was found",value,"time(s) in input text.")