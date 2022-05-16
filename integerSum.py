
def get_sum(a,b):
    return sum(list(range(a,b+1))) if a<b else sum(list(range(b,a+1))) if a>b else a 


print(get_sum(1,3))