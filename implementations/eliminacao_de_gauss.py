from utils.in_out_workers import TxtWorker


def m(x: float, y: float):
    '''x = Mix\n y = Mxx'''
    return x / y


def l(x: float, m: float, y: float):
    '''x = Lx\n m = Mij\n y = Lx-1'''
    return x - m * y


def eliminacao_de_gauss(matriz: list, tamanho: int):
    '''Executa o método da eliminação de Gauss'''

    matriz_resp = [1] * tamanho
    for i in range(tamanho - 1):
        mx = i + 1
        for j in range(i + 1, tamanho):
            mi = m(matriz[mx][i], matriz[i][i])
            mx += 1
            matriz[j][i] = 0
            for k in range(i + 1, tamanho + 1):
                matriz[j][k] = l(matriz[j][k], mi, matriz[i][k])

    matriz_resp[tamanho - 1] = matriz[j][k] / matriz[j][k - 1]

    for i in range(tamanho - 2, -1, -1):
        resp = 0
        for j in range(tamanho):
            if i != j:
                resp += (-matriz[i][j]) * matriz_resp[j]

        resp += matriz[i][j + 1]

        matriz_resp[i] = resp / matriz[i][i]
    return matriz_resp


def run():
    data: TxtWorker = TxtWorker('gauss.txt')
    data.read_matrix()
    answers = []
    for i in range(len(data.matrix)):
        answers.append(eliminacao_de_gauss(data.matrix[i], len(data.matrix[i])))

    data.write_matrix(answers)


run()
