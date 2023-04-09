# Funcional (sem uso de arquivo pq o python me odeia)
from eval_exp_mat import func_parser

'''
    x = Mix
    y = Mxx
'''
def m(x,y):
    return x/y

'''
    x = Lx
    m = Mij
    y = Lx-1
'''
def l(x, m, y):
    return x - m * y

def eliminacao_de_gauss(matriz, tamanho):
    print(matriz)
    matriz_resp = [1] * tamanho
    for i in range(tamanho -1):
        
        mx = i + 1
            
        for j in range(i+1, tamanho):
            mi = m(matriz[mx][i], matriz[i][i])
            mx += 1
            matriz[j][i] = 0
            for k in range(i+1, tamanho + 1):
                matriz[j][k] = l(matriz[j][k], mi, matriz[i][k]) 


    matriz_resp[tamanho-1] = matriz[j][k]/ matriz[j][k-1]
        
    for i in range(tamanho-2, -1, -1):
        resp = 0
        for j in range(tamanho):
            if i != j:
                resp += (- matriz[i][j]) * matriz_resp[j]
            
        resp += (matriz[i][j+1])
            
        matriz_resp[i] = resp/matriz[i][i]


    print(matriz_resp)

MATRIZ = [
    [3.0, -0.1, -0.2,  7.85],
    [0.1,  7.0, -0.3, -19.3],
    [0.3, -0.2, 10.0,  71.4]
]
eliminacao_de_gauss(MATRIZ, len(MATRIZ))

