def cuadrado(n):
    #cuadrado=[["*"]*n  if it==0 or it==n-1 else [" "]*n for it in range(n)   ]
    a=lambda x,y: "*" if x==0 or y ==0 or x==n-1 or y==n-1 else " "
    return [[a(it,it2) for it2 in range(n)] for it in range(n)]

def cuadrado2(n):
    return [[(lambda x,y: "*" if x==0 or y ==0 or x==n-1 or y==n-1 else " ")(column,row) 
            for column in range(n)] for row in range(n)]


a=cuadrado2(10)

for it in a :
    print(it)