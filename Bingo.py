def transponer(mat):
    return [[x for x in y] for y in (list(zip(*mat)))]

def checkBingo(mat):
    for i in mat: 
        if i==[1 for y in range(len(mat))]: return True
    for i in transponer(mat): 
        if i==[1 for y in range(len(mat))]: return True    
    return False

def bingo(mat,arr):
    mI=[[0 for x in range(len(mat))] for y in range(len(mat))]
    for b in arr: 
        print("\nBingo Number: ",b)
        for row in range(len(mat)):
            for column in range(len(mat[row])):
                if mat[row][column]==b : mI[row][column]=1 
        for i in mI: print(i)
        if checkBingo(mI):return b
        
mat=[[ 1, 2, 3,13],
     [ 4, 5, 6,14],
     [ 7, 8, 9,15],
     [10,11,12,16]]

arr=[13,2,1,3,5,6,7,8,9,16,11,12,4,14,10,15]

print("\nEl valor en que se completo el bingo es: ", bingo(mat,arr))