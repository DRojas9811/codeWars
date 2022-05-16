import math
from functools import reduce
def multiply(n):
    return math.prod([int(it) for it in [int(i) for i in str(n)] ])
def persistence(n):
    if len(str(n))==1:return 0
    else: out=[n]
    while(1):
        n=((lambda n1: math.prod([int(it) for it in [int(i) for i in str(n)] ]))(n))
        if len(str(n))==1:break
        out.append(n)
    print(out)
    return len(out)

def persistence2(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        print(newNum)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist


print(persistence(999))
print(persistence2(39))
    

