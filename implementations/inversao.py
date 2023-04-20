from utils.in_out_workers import TxtWorker


def pivotteamento(matrix: list):
    '''Realiza o pivotteamento da matrix na diagonal principal.
    Parâmetros: matrix - matrix em que será feito o pivotteamento.
    '''

    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            elements = []
            for j in range(len(matrix)):
                elements.append(matrix[j][i])
            matrix[i], matrix[elements.index(max(elements))] = (
                matrix[elements.index(max(elements))],
                matrix[i],
            )


def inversa_gauss_jordan(matrix: list):
    '''Realiza o cálculo da inversa a partir do método de Gauss-Jordan.
    Parâmetros: matrix - matrix que será calculada a inversa.
    Retorno: inversa - matrix inversa calculada.
    '''

    pivotteamento(matrix)
    identity = []
    for i in range(len(matrix)):
        aux = []
        for j in range(len(matrix[0])):
            if i == j:
                aux.append(1)
            else:
                aux.append(0)
        identity.append(aux)

    complete_matrix = []
    for i in range(len(matrix)):
        complete_matrix.append(matrix[i] + identity[i])

    for i in range(len(matrix)):
        pivot = complete_matrix[i][i]
        for j in range(len(matrix[0]) * 2):
            complete_matrix[i][j] /= pivot

        pivot = complete_matrix[i][i]

        for j in range(len(matrix)):
            if j == i:
                continue
            m = complete_matrix[j][i] / pivot
            for k in range(len(matrix[0]) * 2):
                complete_matrix[j][k] = complete_matrix[j][k] - (
                    m * complete_matrix[i][k]
                )

    reverse = []
    for linha in complete_matrix:
        meio = int(len(linha) / 2)
        parte_da_linha = linha[meio:]
        parte_da_linha.pop(-1)
        reverse.append(parte_da_linha)

    return reverse


def run():
    data: TxtWorker = TxtWorker('inversion.txt')
    data.read_matrix()
    answers = []
    for i in range(len(data.matrix)):
        answers.append(inversa_gauss_jordan(data.matrix[i]))

    data.write_matrix(answers)


run()
