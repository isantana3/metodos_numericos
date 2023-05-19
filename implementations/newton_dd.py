from utils.in_out_workers import TxtWorker
from sympy import symbols, simplify

REFERENCE_TABLE = {}


def calc_bn(list_x: list, list_y):
    if len(list_x) == 2:
        result = (list_y[1] - list_y[0]) / (list_x[1] - list_x[0])
        REFERENCE_TABLE[str(list_x)] = result
        return result
    try:
        left_ref = REFERENCE_TABLE[str(list_x[1:])]
    except:
        left_ref = calc_bn(list_x[1:], list_y[1:])
    try:
        right_ref = REFERENCE_TABLE[str(list_x[:-1])]
    except:
        right_ref = calc_bn(list_x[:-1], list_y[:-1])

    result = (left_ref - right_ref) / (list_x[-1] - list_x[0])
    REFERENCE_TABLE[str(list_x)] = result
    return result


def resolve_coefficients(coefficients: list, list_x: list):
    expression = coefficients[0]
    x = symbols('x')
    for i in range(1, len(coefficients)):
        exp = coefficients[i]
        for j in range(i):
            exp *= x - list_x[j]
        expression += exp
    return simplify(expression)


def ddn(x: list, y: list):
    '''
    X são os valores de x0, x1, x2, x3... xn \n
    Y são os valores de f(x0), f(x2), f(x3)... f(xn)
    '''
    length = len(x)
    coefficients = []
    coefficients.append(y[0])
    x.reverse()
    y.reverse()
    for i in range(length - 2, 0, -1):
        coefficients.append(calc_bn(x[i:], y[i:]))
    coefficients.append(calc_bn(x, y))
    x.reverse()
    response = resolve_coefficients(coefficients, x)
    return f'f{len(x)-1}(X) = {response}'


def run():
    data: TxtWorker = TxtWorker('newton_dd.txt')
    data.read_2d_points()
    answers = []
    for i in range(len(data.point_x)):
        answers.append(ddn(data.point_x[i], data.point_y[i]))

    data.write_lines(answers)


run()
