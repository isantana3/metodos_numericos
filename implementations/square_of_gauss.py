import math
from utils.eval_exp_mat import func_parser


def gauss_quadrature(f, a, b, n):
    # Coeficientes e pontos de Gauss-Legendre
    x, w = compute_gauss_legendre_points(n)

    # Transformação para o novo intervalo de integração
    t = 0.5 * (b - a) * x + 0.5 * (a + b)

    # Avaliação da função nos pontos de Gauss-Legendre
    y = [f(ti) for ti in t]

    # Cálculo da integral aproximada considerando a mudança de variáveis
    integral = 0.5 * (b - a) * sum(w[i] * y[i] for i in range(n))

    return integral


def compute_gauss_legendre_points(n):
    # Tabela de pontos e pesos de Gauss-Legendre pré-computados
    # para diferentes valores de n
    gauss_legendre_table = {
        1: ([0], [2]),
        2: ([-1 / math.sqrt(3), 1 / math.sqrt(3)], [1, 1]),
        3: ([-math.sqrt(3 / 5), 0, math.sqrt(3 / 5)], [5 / 9, 8 / 9, 5 / 9]),
        4: (
            [
                -math.sqrt((3 + 2 * math.sqrt(6 / 5)) / 7),
                -math.sqrt((3 - 2 * math.sqrt(6 / 5)) / 7),
                math.sqrt((3 - 2 * math.sqrt(6 / 5)) / 7),
                math.sqrt((3 + 2 * math.sqrt(6 / 5)) / 7),
            ],
            [
                (18 - math.sqrt(30)) / 36,
                (18 + math.sqrt(30)) / 36,
                (18 + math.sqrt(30)) / 36,
                (18 - math.sqrt(30)) / 36,
            ],
        ),
    }

    if n not in gauss_legendre_table:
        raise ValueError("Número de pontos de Gauss-Legendre inválido.")

    return gauss_legendre_table[n]


# Exemplo de função para integrar
func = '0.2+25*x-200*x^2+675*x^3-900*x^4+400*x^5'


def f(x: float):
    '''Calculate the function'''
    func = func.replace('x', str(x))
    return func_parser(func)


# Função de mudança de variáveis
def change_of_variables(x):
    # Função de mudança de variáveis (exemplo: transformação logarítmica)
    return math.log(x + 2)


# Intervalo de integração
a = 0
b = 2

# Número de pontos de Gauss-Legendre
n = 4

# Cálculo da integral usando a quadratura de Gauss com mudança de variáveis
integral = gauss_quadrature(lambda x: f(change_of_variables(x)), a, b, n)

print("Integral aproximada:", integral)
