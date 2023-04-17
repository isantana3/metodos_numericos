from utils.eval_exp_mat import func_parser
from utils.in_out_workers import TxtWorker
import math


def secante(a: float, b: float, erro: float, function: str, max_iterations: float):
    i = 0

    while i < max_iterations:
        fa = solve_func(a, function)
        fb = solve_func(b, function)
        x = (fb * a - fa * b) / (fb - fa)
        fx = solve_func(x, function)
        interval = (b - a) / 2
        if abs(fx) < erro or interval < erro:
            return {'function': function.strip('\n'), 'solution': f'X{i+1} = {x}'}
        a, b = b, x
        i += 1
    return {'function': function.strip('\n'), 'solution': f'X{i} = {x}'}


def solve_func(x, func):
    '''Calculate the function'''
    func = func.replace('x', str(x))
    return func_parser(func)


def run():
    data: TxtWorker = TxtWorker('secante.txt')
    data.read_bissection()
    print(data.funcao[0])
    answers = []
    for i in range(len(data.funcao)):
        max_iterations = math.ceil(
            math.log((data.b[i] - data.a[i]) / data.error[i])
            / math.log((1 + math.sqrt(5)) / 2)
        )
        answers.append(
            secante(
                a=data.a[i],
                b=data.b[i],
                erro=data.error[i],
                function=data.funcao[i],
                max_iterations=max_iterations,
            )
        )
    data.write_bissection(answers)


run()
