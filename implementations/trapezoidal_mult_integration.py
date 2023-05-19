from utils.eval_exp_mat import func_parser
from utils.in_out_workers import TxtWorker


def multi_trapezoidal_integration(function: str, a: float, b: float):
    h = (b - a) / 10
    response = 0
    points = [a]
    for i in range(10):
        points.append(points[i] + h)

    for i in range(10):
        fa = solve_func(points[i], function)
        fb = solve_func(points[i + 1], function)
        response += h * (fa + fb) / 2

    return f'Itegration of {function} is: {response}'


def solve_func(x: float, func: str):
    '''Calculate the function'''
    func = func.replace('x', str(x))
    return func_parser(func)


def run():
    data: TxtWorker = TxtWorker('multi_itegration.txt')
    data.read_function()
    answers = []
    for i in range(len(data.a)):
        answers.append(
            multi_trapezoidal_integration(data.funcao[i], data.a[i], data.b[i])
        )
    data.write_lines(answers)


run()
