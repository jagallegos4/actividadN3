import numpy as np

A=np.array([[7,1,-1,2], #Se define la matriz A
            [1,8,0,-2],
            [-1,0,4,-1],
            [2,-2,-1,6]])

b=np.array([3,-5,4,-3]) #Se define la matriz de terminos independientes

x= np.zeros(len(b))  #se define x0=[0,0,0,0]
n=100 #se define el numero maximo de iteraciones

def sor(A,b,x,n=100,w=1.1):
    for k in range(n):
        for i in range(len(b)):
            x[i] =(1-w)*x[i]+(b[i] - np.sum(A[i][:i] * x[:i])
                    - np.sum(A[i][i + 1:] * x[i + 1:]))*(w/A[i][i])

        e = np.linalg.norm(A @ x - b)
        print("Paso N°:", k + 1,"x:", x, "Error:",e)
        if e < 1e-8:
            break
    return x

x=sor(A,b,x)

print("Solucion del sistema con el metodo Gauss-Seidel:",x)