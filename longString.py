def longest(a1, a2):
    return "".join(sorted(list(set(a1+a2))))
    

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a,b))