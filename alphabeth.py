import string

def funci(strg):
    alp=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    for it in alp:
        if strg.lower().find(it)==-1:
            print(it)
            return False
    return True


def is_pangram(s):
    print(set(string.ascii_lowercase))   
    ##print(set(s.lower()))
    return set(string.ascii_lowercase) <= set(s.lower())


text="Cwm fjord bank glyphs vext quiz"
print(funci(text))
print(is_pangram(text))