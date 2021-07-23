import numpy as np

A=np.array([[7,1,-1,2], #Se define la matriz A
            [1,8,0,-2],
            [-1,0,4,-1],
            [2,-2,-1,6]])

b=np.array([3,-5,4,-3]) #Se define la matriz de terminos independientes

x0=np.zeros(len(b)) #se define x0=[0,0,0,0]

def jacobi(A,b,x0,eps=1e-9,n=100): #funcion jacobi
    D=np.diag(np.diag(A))
    LU=A-D
    x=x0
    for i in range(n):
        D_inv=np.linalg.inv(D)
        xTemp=x
        x=np.dot(D_inv,np.dot(-(LU),x)+b)
        e = np.linalg.norm(x - xTemp)
        print("Paso N°",i+1, "x:", x, "Error:",e)

        if e< eps:
            return x
    return x

x=jacobi(A,b,x0)

print("Solucion del sistema con el metodo jacobi:",x)