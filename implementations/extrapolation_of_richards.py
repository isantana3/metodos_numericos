from utils.eval_exp_mat import func_parser
from utils.in_out_workers import TxtWorker


def trapezoidal_integration(function: str, a: float, b: float, n: int = 10):
    h = (b - a) / n
    response = 0
    points = [a]
    for i in range(n):
        points.append(points[i] + h)

    for i in range(n):
        fa = solve_func(points[i], function)
        fb = solve_func(points[i + 1], function)
        response += h * (fa + fb) / 2

    return response


def solve_func(x: float, func: str):
    '''Calculate the function'''
    func = func.replace('x', str(x))
    return func_parser(func)


def richards(function: str, a: float, b: float, n1: int = 2, n2: int = 4):
    h1 = (b - a) / n1
    h2 = (b - a) / n2
    i1 = trapezoidal_integration(function, a, b, n1)
    i2 = trapezoidal_integration(function, a, b, n2)

    response = i2 + (i2 - i1) / ((h1 / h2) ** 2 - 1)

    return f'Itegration of {function} is: {response}'


def run():
    data: TxtWorker = TxtWorker('richards.txt')
    data.read_integration()
    answers = []
    for i in range(len(data.a)):
        answers.append(
            richards(data.funcao[i], data.a[i], data.b[i], data.n1[i], data.n2[i])
        )
    data.write_lines(answers)


run()
