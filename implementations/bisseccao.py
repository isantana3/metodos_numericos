from utils.eval_exp_mat import func_parser
from utils.in_out_workers import TxtWorker
import math


def bisseccao(a: float, b: float, erro: float, function: str, max_iterations: float):
    '''Find the zero of a function with bissection method'''
    i = 0
    while i < max_iterations:
        fa = solve_func(a, function)
        c = (a + b) / 2
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
    data: TxtWorker = TxtWorker('bissection.txt')
    data.read_function()
    answers = []
    for i in range(len(data.funcao)):
        max_iterations = math.ceil(math.log2((data.b[i] - data.a[i]) / data.error[i]))
        answers.append(
            bisseccao(
                a=data.a[i],
                b=data.b[i],
                erro=data.error[i],
                function=data.funcao[i],
                max_iterations=max_iterations,
            )
        )

    data.write_function_solution(answers)


run()
