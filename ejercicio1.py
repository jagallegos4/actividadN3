import numpy as np

A=np.array([[6,0,0,0], #Se define la matriz L
            [3,6,0,0],
            [4,-2,7,0],
            [5,-3,9,21]])

b=np.array([12,-12,14,-2]) #Se define los terminos independientes

def sus_prog(L, x): #se define el metodo de la sustitucion progresiva
    n=len(x)
    x=np.zeros(n)
    for i in range(n):
        sumj=0
        for j in range(i):
            sumj+=L[i,j]*x[j]
        x[i]=(b[i]-sumj)/L[i,i]
    return x

z=sus_prog(A,b)
print("Solucion de Sistema de Ecuaciones: ",z)