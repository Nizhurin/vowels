vowels = ['a', 'e', 'i', 'o', 'u']
found = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

word = input("Provide a text to search for vowels: ")

for letter in word:
    if letter.lower() in vowels:
        found[letter.lower()] += 1
print("Vowels - Count vowels in input text ")
for key,value in sorted(found.items()):
    print(key,"was found",value,"time(s).")