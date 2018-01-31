def search4vowels(phrase:str) -> set:
    """Выводит гласные, найденные во введенном слове."""
    vowels = set('aeiou')
    found = vowels.intersection(set(phrase))
    return found

def search4letters(phrase:str, letters:str='aeiou') -> set:
    """This function search letters in input phrase."""
    return set(letters).intersection(set(phrase))

print(search4vowels('hitchhiker'))
print(search4letters('hitcjhiker'))
