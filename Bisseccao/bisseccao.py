# Testado e funcional (sem uso de arquivo pq o python me odeia)
import math
from utils.eval_exp_mat import func_parser

ENTRADA1 = 'input1.txt'
ENTRADA2 = 'input2.txt'
ENTRADA3 = 'input3.txt'


def bisseccao(a, b, erro, function):

    i = 0
    while True:
        fa = solve_func(a, function)

        fb = solve_func(b, function)
        c = (a + b) / 2
        fc = solve_func(c, function)
        if abs(fc) < erro:
            return c

        elif (fa * fc) < 0:
            b = c

        else:

            a = c


# Resolver uma função
def solve_func(x, func):
    func = func.replace('x', str(x))
    return func_parser(func)


def main():

    print("QUESTÃO 1")
    ### Questão 1
    function = '1-(1+x+x^2/2)*E^(-x)-0.1'
    a = '0'
    b = '10'
    error = '0.009'

    print("Resposta: " + str(bisseccao(float(a), float(b), float(error), function)))

    function = '1-(1+x+x^2/2)*E^(-x)-0.9'
    a = '0'
    b = '10'
    error = '0.009'

    print("Resposta: " + str(bisseccao(float(a), float(b), float(error), function)))

    print("QUESTÃO 2")
    # Questão 2
    function = '((sin(x)*cos(x))/((1/1.25)-cos(x)^2))-tan(80/2)'
    a = '0'
    b = '60'
    error = '0.009'

    print("Resposta: " + str(bisseccao(float(a), float(b), float(error), function)))


main()
