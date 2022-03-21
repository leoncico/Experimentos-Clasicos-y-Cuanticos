import Libreria as lc
import math
import matplotlib.pyplot as plt

def main():
    #1
    print("Experimentos Probabilistico con Canicas:")

    print("Matriz asociada:")
    matriz = [ [0,0,0,0,1,0], [0,0,0,1,0,0], [0,0,0,0,0,0], [1,0,0,0,0,0], [0,0,1,0,0,0], [0,1,0,0,0,1] ]

    for i in matriz:
        print(i)
    tics = 2
    X = [x[:] for x in matriz]

    for i in range(2, tics + 1):
        X = lc.multmatrices(X, matriz)

    print("Estado inicial:")
    v_inicial = [ [3],[2],[5],[9],[0],[7] ]

    print("Numero de tics:", tics)

    for i in v_inicial:
        print(v_inicial)

    posicion = lc.accionmatrizvector(X, v_inicial)

    print("Vector Final:")
    print(posicion)
    plt.bar(lc.n_tics(v_inicial), posicion, facecolor="red")
    plt.title("Resultado")
    plt.xlabel("Posicion")
    plt.ylabel("# de Canicas")
    plt.show()
    plt.savefig("Canicas.png")


    #2
    print("Experimento Probabilistico con multiples rendijas")
    print("Matriz asociada:")
    matriz = [[0,0,0,0,0,0,0,0],
            [1/2,0,0,0,0,0,0,0],
            [1/2,0,0,0,0,0,0,0],
            [0,1/3,0,1,0,0,0,0],
            [0,1/3,0,0,1,0,0,0],
            [0,1/3,1/3,0,0,1,0,0],
            [0,0,1/3,0,0,0,1,0],
            [0,0,1/3,0,0,0,0,1]]

    for i in matriz:
        print(i)

    tics = 2
    X = [x[:] for x in matriz]

    for i in range(2, tics + 1):
        X = lc.multmatrices(X, matriz)

    print("Estado inicial:")
    v_inicial = [[1], [0], [0], [0], [0], [0], [0], [0]]

    print("Numero de tics:", tics)

    for i in v_inicial:
        print(i)
    posicion = lc.accionmatrizvector(X, v_inicial)

    print("Vector Final")
    print(posicion)
    lc.graficas(lc.n_tics(matriz), posicion)


    #3
    print("Experimento Cuantico con 2 rendijas")
    matriz = [[(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
            [(1/math.sqrt(2),0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
            [(1/math.sqrt(2),0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
            [(0,0), (-1/math.sqrt(6),1/math.sqrt(6)), (0,0), (1,0), (0,0), (0,0), (0,0), (0,0)],
            [(0,0), (-1/math.sqrt(6),-1/math.sqrt(6)), (0,0), (0,0), (1,0), (0,0), (0,0), (0,0)],
            [(0,0), (1/math.sqrt(6),-1/math.sqrt(6)), (-1/math.sqrt(6),1/math.sqrt(6)), (0,0), (0,0), (1,0), (0,0), (0,0)],
            [(0,0), (0,0), (-1/math.sqrt(6),-1/math.sqrt(6)), (0,0), (0,0), (0,0), (1,0), (0,0)],
            [(0,0), (0,0), (1/math.sqrt(6),-1/math.sqrt(6)), (0,0), (0,0), (0,0), (0,0), (1,0)]]
    print("Matriz Asociada: ")

    for i in matriz:
        print(i)
    tics = 3

    X = [x[:] for x in matriz]
    for i in range(2, tics + 1):
        X = lc.productomatricesComplex(X, matriz)
    print("Estado inicial: ")
    v_inicial = [[(1,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)]]

    print("Numero de tics:",tics)
    for i in v_inicial:
        print(i)
    posicion = lc.accmatriz_vectorcplx(X, v_inicial)

    print("Vector Final")
    probabilidades = []
    for i in range(len(posicion)):
        probabilidades += [(lc.modulocplx(posicion[i]))**2]
    for i in probabilidades:
        print(i)
    lc.graficas(lc.n_tics(matriz), probabilidades)
main()