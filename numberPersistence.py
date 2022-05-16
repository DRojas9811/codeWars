import numpy
def multiply(n):
    numpy.prod()
    a=[int(it) for it in list(set(str(n))) ]
    print(a)
    value=1
    for i in str(n): value=value*int(i)
    return value
def persistence(n):
    v=n
    while(1):
        v=multiply(v)
        if len(str(v))==1:
            break
        print(v)
    return v

print(persistence(999))
    

