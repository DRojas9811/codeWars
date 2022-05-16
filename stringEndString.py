##solution('abc', 'bc') # returns true
##solution('abc', 'd') # returns false
def solution(string, ending):
    for it in range(1,len(ending)+1):
        try:
            if string[-it]!=ending[-it]:
                return False
        except IndexError:
            return False
    return True

string="hola"
ending="ola"
print(solution(string,ending))


solution = lambda s,e: s[-len(e):] == e 
s="hola"
e="ola"
##print(s[-1:])
print(solution(s,e))