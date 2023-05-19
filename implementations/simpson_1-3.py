from utils.eval_exp_mat import func_parser
from utils.in_out_workers import TxtWorker


def solve_points(results: list):
    times_4 = 0
    times_2 = 0
    for i in range(1, len(results) - 1):
        if i % 2 == 0:
            times_2 += results[i]
        else:
            times_4 += results[i]

    return results[0] + 4 * times_4 + 2 * times_2 + results[-1]


def simpson_1_3(function: str, a: float, b: float, n: int = 4):
    h = b - a
    response = 0
    points = [a]
    fx = []
    for i in range(n):
        points.append(points[i] + h / n)

    for i in range(n + 1):
        fx.append(solve_func(points[i], function))

    response = h * solve_points(fx) / (3 * n)
    return f'Itegration of {function} is: {response}'


def solve_func(x: float, func: str):
    '''Calculate the function'''
    func = func.replace('x', str(x))
    return func_parser(func)


def run():
    data: TxtWorker = TxtWorker('simpson_13.txt')
    data.read_function()
    answers = []
    for i in range(len(data.a)):
        answers.append(simpson_1_3(data.funcao[i], data.a[i], data.b[i]))
    data.write_lines(answers)


run()
