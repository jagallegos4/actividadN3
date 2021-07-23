import numpy as np

A=np.array([[2,1,-1,2], #Se define la matriz A
            [1,1,5,-2],
            [-1,0,4,-1],
            [-5,-2,-1,-8]])

def frob(A):
    n=len(A)
    s=0
    for k in range(n):
        for i in range(n):
            s=s+(A[k,i])**2
        N=np.sqrt(s)
    return N

N=frob(A)

print("La norma de Frobenius es:",N)