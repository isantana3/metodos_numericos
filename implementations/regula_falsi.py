from utils.eval_exp_mat import func_parser
from utils.in_out_workers import TxtWorker
import math


def regula_falsi(a: float, b: float, erro: float, function: str, max_iterations: float):
    '''Find the zero of a function with bissection method'''
    i = 0
    while i < max_iterations:
        fa = solve_func(a, function)
        fb = solve_func(b, function)
        c = (a * fb - b * fa) / (fb - fa)
        fc = solve_func(c, function)
        interval = (b - a) / 2
        if abs(fc) < erro or interval < erro:
            return {'function': function.strip('\n'), 'solution': f'X{i+1} = {c}'}
        elif (fa * fc) < 0:
            b = c
        else:
            a = c
        i += 1
    return {'function': function.strip('\n'), 'solution': f'X{i} = {c}'}


def solve_func(x: float, func: str):
    '''Calculate the function'''
    func = func.replace('x', str(x))
    return func_parser(func)


def run():
    data: TxtWorker = TxtWorker('regula_falsi.txt')
    data.read_bissection()
    answers = []
    for i in range(len(data.funcao)):
        max_iterations = math.ceil(math.log2((data.b[i] - data.a[i]) / data.error[i]))
        answers.append(
            regula_falsi(
                a=data.a[i],
                b=data.b[i],
                erro=data.error[i],
                function=data.funcao[i],
                max_iterations=max_iterations,
            )
        )

    data.write_bissection(answers)


run()
