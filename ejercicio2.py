import numpy as np

A=np.array([[4,6,10], #Se define la Matriz A
            [6,25,19],
            [10,19,62]])

B=np.array([[4,6,10],
            [6,3,19],
            [10,19,62]])
#Funcion que calcula la matriz L
def cholesky(M):
    n=np.shape(M)
    m,_=np.shape(M)
    L=np.zeros(n)
    for j in range(m):
        for i in range(j,m):
            if i==j:
                L[i,j]=np.sqrt(M[i,j]-np.sum(L[i,:j]**2))
            else:
                L[i,j]=(M[i,j]-np.sum(L[i,:j]))/L[j,j]
    return L

#Calculando la matriz L de A
L=cholesky(A)
LB=cholesky(B)
#print("Matriz L: \n",L)
print("Matiz L:\n",LB)

#calculando la Matriz L traspuesta
Lt=np.transpose(L)
LtB=np.transpose(LB)
#print("Matriz Lt: \n",Lt)
print("Matrz Lt:\n",LtB)