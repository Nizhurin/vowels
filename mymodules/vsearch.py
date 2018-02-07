def search4vowels(phrase: str) -> set:
    """Выводит гласные, найденные во введенном слове."""
    vowels = set('aeiou')
    found = vowels.intersection(set(phrase))
    return found


def search4letters(phrase: str, letters: str='aeiou', ignore_case: bool=False) -> dict:
    """This function search letters in input phrase."""
    mydict = {}
    if bool(ignore_case):
        phrase = phrase.lower()
        letters = letters.lower()
    for char in phrase:
        if char in letters:
            mydict.setdefault(char,0)
            mydict[char] += 1
    if bool(mydict) == False:
        mydict['No found letters in input phrase'] = 0
    return mydict

