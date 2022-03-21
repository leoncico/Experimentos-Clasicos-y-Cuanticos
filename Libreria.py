import math
import matplotlib.pyplot as plt

def sumacplx(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)

def productocplx(a, b):
    real = (a[0] * b[0]) - (a[1] * b[1])
    img = (a[0] * b[1]) + (a[1] * b[0])
    return (real, img)

def modulocplx(a):
    return math.sqrt((a[0])**2 + (a[1])**2)

def accionmatrizvector(A, v):
    f = len(A)
    c = len(A[0])
    m = []
    for i in range(f):
        suma = 0
        for j in range(c):
            suma = suma + A[i][j] * v[j][0]
        m = m + [suma]
    return m

def multmatrices(A, B):
    f = len(A)
    c = len(A[0])
    m = []
    for i in range(f):
        fila = []
        for j in range(f):
            suma = 0
            for k in range(c):
                suma = suma + A[i][k] * B[k][j]
            fila = fila + [suma]
        m = m + [fila]
    return m

def productomatricesComplex(A, B):
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(filas):
            suma = (0,0)
            for k in range(columnas):
                suma = sumacplx(suma, productocplx(A[i][k], B[k][j]))
            fila = fila + [(suma)]
        matriz = matriz + [fila]
    return matriz

def accmatriz_vectorcplx(A, v):
    f = len(A)
    c = len(A[0])
    m = []
    for i in range(f):
        suma = (0,0)
        for j in range(c):
            suma = sumacplx(suma, productocplx(A[i][j], v[j][0]))
        m = m + [(suma)]
    return m

def n_tics(matriz):
    tics = []
    for i in range(len(matriz)):
        tics = tics + [i]
    return tics

def graficas(posicion, v):
    plt.bar(posicion, v, facecolor = "lime")
    plt.title("Gráfica de Probabilidades Finales")
    plt.xlabel("Posiciones")
    plt.ylabel("Probabilidad")
    plt.show()
    plt.savefig('Probabilidades.png')