from utils.eval_exp_mat import func_parser
from utils.in_out_workers import TxtWorker
import sympy as sp


def derivate(function: str):
    '''Derivate an function F(x), but not solve the problem'''

    x = sp.Symbol('x')
    df = sp.diff(function, x, 1)
    return str(df)


def newton_raphson(x1: float, erro: float, function: str):
    derivate_function = derivate(function)
    i = 0
    while i < 30:
        fx = solve_func(x1, function)
        ffx = solve_func(x1, derivate_function)
        x1 = x1 - (fx / ffx)
        if solve_func(x1, function) < erro:
            return {'function': function.strip('\n'), 'solution': f'X{i} = {x1}'}
        i += 1
    return {'function': function.strip('\n'), 'solution': f'X{i} = {x1}'}


def solve_func(x: float, func: str):
    '''Calculate the function'''
    func = func.replace('x', str(x))
    return func_parser(func)


def run():
    data: TxtWorker = TxtWorker('newton_raphson.txt')
    data.read_newton_raphson()
    answers = []
    for i in range(len(data.funcao)):
        answers.append(
            newton_raphson(x1=data.a[i], erro=data.error[i], function=data.funcao[i])
        )

    data.write_function_solution(answers)


run()
