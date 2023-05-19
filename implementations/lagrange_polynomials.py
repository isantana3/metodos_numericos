from utils.in_out_workers import TxtWorker
from sympy import symbols, Poly

X = symbols('X')


def build_polynomial(list_x: list):
    result = []
    for i in range(len(list_x)):
        lk = evaluate_lk(list_x, i, X) / evaluate_lk(list_x, i, list_x[i])
        result.append(lk)
    return result


def evaluate_lk(list_x, i, x):
    result = 1
    for j in range(len(list_x)):
        if j != i:
            result *= x - list_x[j]
    return result


def lagrange(y, list_lk):
    response = ''
    result = 0
    for i in range(len(y)):
        result += y[i] * list_lk[i]
    polynomial = Poly(result, X).coeffs()
    for i in range(len(polynomial)):
        b = pow(X, len(polynomial) - i - 1)
        c = eval(str(b))
        if polynomial[i] > 0:
            response += f'+'
        response += f'{polynomial[i]}*{c} '
    return response


def run():
    data: TxtWorker = TxtWorker('lagrange.txt')
    data.read_2d_points()
    answers = []
    for i in range(len(data.point_x)):
        lk_list = build_polynomial(data.point_x[i])
        answers.append(lagrange(data.point_y[i], lk_list))

    data.write_lines(answers)


run()
