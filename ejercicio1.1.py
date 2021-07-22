import numpy as np

A=np.array([[6,0,0,0], #Se define la matriz L
            [3,6,0,0],
            [4,-2,7,0],
            [5,-3,9,21]])


n=np.shape(A)
m,_=np.shape(A)
#se inicializa en ceros las matrices L y U
l=np.zeros(n)
u=np.zeros(n)

#Implementacion del algoritmo para calcular las matrices L y U
for j in range(m):
    l[j,j]=1
    for i in range (j+1,m):
        l[i,j]=A[i,j]/A[j,j]
        for k in range(j+1,m):
            A[i,k]=A[i,k]-l[i,j]*A[j,k]
    for k in range(j,m):
        u[j,k]=A[j,k]

#Se imprimen resultados
print("La matriz L es: \n",l)
print("La matriz U es: \n",u)

