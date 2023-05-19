from utils.eval_exp_mat import func_parser
from utils.in_out_workers import TxtWorker
import math


def simple_trapezoidal_integration(function: str, a: float, b: float):
    fa = solve_func(a, function)
    fb = solve_func(b, function)
    h = b - a
    response = h * (fa + fb) / 2
    return f'Itegration of {function} is: {response}'


def solve_func(x: float, func: str):
    '''Calculate the function'''
    func = func.replace('x', str(x))
    return func_parser(func)


def run():
    data: TxtWorker = TxtWorker('itegration.txt')
    data.read_function()
    answers = []
    for i in range(len(data.a)):
        answers.append(
            simple_trapezoidal_integration(data.funcao[i], data.a[i], data.b[i])
        )
    data.write_lines(answers)


run()
