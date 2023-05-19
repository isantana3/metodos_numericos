from utils.eval_exp_mat import func_parser
from utils.in_out_workers import TxtWorker
import math


def derivate(function: str, right: float, left: float, h: float):
    print(f'rgt: {right}')
    print(f'lft: {left}')
    return (solve_func(right, function) - solve_func(left, function)) / h


def first_order(function: str, right_x: float, left_x: float):
    middle_x = (left_x + right_x) / 2
    h = middle_x - left_x
    h2 = right_x - left_x
    return (
        derivate(function, middle_x, left_x, h),
        derivate(function, right_x, left_x, h2),
        derivate(function, right_x, middle_x, h),
    )


def second_order(function: str, right_x: float, left_x: float):
    middle_x = (left_x + right_x) / 2
    h = middle_x - left_x
    right = derivate(function, right_x, middle_x, h)
    left = derivate(function, middle_x, left_x, h)
    return derivate(function, right, left, h)


def solve_func(x: float, func: str):
    '''Calculate the function'''
    try:
        func = func.replace('x', str(x)).strip('\n')
        return eval(func)
    except:
        import pdb

        pdb.set_trace()


def run():
    data: TxtWorker = TxtWorker('derivation.txt')
    data.read_function()
    answers = []
    for i in range(len(data.a)):
        aux = []
        aux.append(first_order(data.funcao[i], data.a[i], data.b[i]))
        aux.append(second_order(data.funcao[i], data.a[i], data.b[i]))
        answers.append(aux)
    data.write_derivation(answers)


run()
