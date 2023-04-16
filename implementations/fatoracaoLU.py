# Funcional (sem uso de arquivo pq o python me odeia)
from decimal import Decimal

def somatorioU(i, j, k, L, U):
    total = 0.0
    while True:
        total += L[i][k] * U[k][j]
        k += 1
        if k > i-1:
            break
    return total

def somatorioL(i, j, k, L, U):
    total = 0.0
    while True:
        total += L[i][k] * U[k][j]
        k += 1
        if k > j-1:
            break
    return total


def fatoracaoLU(matriz, tamanho):

    L = []
    U = []
    for i in range(tamanho):
        auxL = []
        auxU = []
        for j in range(tamanho):
            if i == j:
                auxL.append(1)
                auxU.append(0)
            else: 
                auxL.append(0)
                auxU.append(0)
        L.append(auxL)
        U.append(auxU)


    for i in range(tamanho):
        U[0][i] = matriz[0][i]
        L[i][0] = float(Decimal(str(matriz[i][0])) / Decimal(str(matriz[0][0])))
        # print(U)

    for i in range(1, tamanho):
        for j in range(1, tamanho):
            if i <= j:
                U[i][j] = matriz[i][j] - somatorioU(i, j, 0, L, U)
                if i != j:
                    L[i][j] = 0

            else:
                L[i][j] = (matriz[i][j] - somatorioL(i, j, 0, L, U)) / U[j][j]
                U[i][j] = 0


    y = [1] * tamanho
    y[0] = matriz[0][tamanho]
    for i in range (1, tamanho):
        resp = 0
        for j in range (tamanho):
            if j != i:
                resp += (-L[i][j]) * y[j]
        resp += (matriz[i][j+1])
        y[i] = resp/L[i][i]


    x = [1] * tamanho
    x[tamanho-1] = y[tamanho-1] / U[tamanho-1][tamanho-1]
    for i in range (tamanho - 2, -1, -1):
        resp = 0
        for j in range (tamanho):
            if i != j:
                resp += (- U[i][j]) * x[j]
            
        resp += y[i]
            
        x[i] = resp/U[i][i]

    print(x)

print("QUESTÃO 5.1")
# Matriz usada para a questão 5.1 da pg 185
MATRIZ = [
    [ 4, -1,  0, -1,  0,  0, 100],
    [-1,  4, -4, -1,  0, -1,   0],
    [ 0, -1,  4,  0,  0, -1,   0],
    [ 0, -1,  0, -1,  4, -1, 100],
    [ 0,  0, -1,  0, -1,  4,   0]
] 

fatoracaoLU(MATRIZ, len(MATRIZ))

print("QUESTÃO 5.5")
# Matriz usada para a questão 5.5 da pg 188
MATRIZ = [
    [ 4, -1,  0,  1,  0,  0, 0, 0, 0, -50],
    [ 1, -4,  1,  0,  1,  0, 0, 0, 0, -50],
    [ 0,  1, -4,  0,  0,  1, 0, 0, 0,-150],
    [ 1,  0,  0, -4,  1,  0, 1, 0, 0,   0],
    [ 0,  1,  0,  1, -4,  1, 0, 1, 0,   0],
    [ 0,  0,  1,  0,  1, -4, 0, 0, 1,-100],
    [ 0,  0,  0,  0,  1,  0,-4, 1, 0, -50],
    [ 0,  0,  0,  0,  1,  0, 1,-4, 1, -50],
    [ 0,  0,  0,  0,  0,  1, 0, 1,-1,-150]
] 

fatoracaoLU(MATRIZ, len(MATRIZ))