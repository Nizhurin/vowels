phrase = "Don`t panic!"
plist = list(phrase)
print(phrase)
print(plist)
plist.pop(0)
plist[2]=' '
plist[4]=plist.pop(6)
for i in range(4):
    plist.pop()
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)