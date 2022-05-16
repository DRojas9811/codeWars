
import time
start = time.time()


def Fibo(n:int):
    #0,1,1,2,3,5,8,13,21,34,55,89144,233,...
    return n if n <= 1 else (Fibo(n-1) + Fibo(n-2))


def productFib(prod):
    cont=0
    while(1):
        na=Fibo(cont)
        nb=Fibo(cont+1)
        print("na ",na," y nb ",nb, " resultaddo ",na*nb)
        value=True if na*nb==prod else False
        if na*nb>=prod:
            break
        else:cont=cont+1   
    return [na,nb,value]
    
print(productFib(1000000))

end = time.time()
total_time = end - start
print("\n"+ str(total_time))