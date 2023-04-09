# Testado e funcional (sem uso de arquivo pq o python me odeia)
from utils.eval_exp_mat import func_parser


def secante(a, b, erro, function):
    k = 0

    while True:
        fa = solve_func(a, function)
        fb = solve_func(b, function)
        x = (fb * a - fa * b) / (fb - fa)
        fx = solve_func(x, function)

        if abs(fx) < erro:
            break
        a, b = b, x
        k += 1

    print("k = " + str(k))
    print("x = " + str(x))
    print("erro = " + str(fx))


# Resolver uma função
def solve_func(x, func):
    func = func.replace('x', str(x))
    return func_parser(func)


print("QUESTÃO 1")
# Questão 1
function = '((sin(x)*cos(x))/((1/1.25)-cos(x)^2))-tan(80/2)'
a = '0'
b = '60'
error = '0.009'
secante(float(a), float(b), float(error), function)


# Questão 1
function = '((sin(x)*cos(x))/((1/1.25)-cos(x)^2))-tan(80/2)'
a = '0'
b = '60'
error = '0.009'
secante(float(a), float(b), float(error), function)

print("QUESTÃO 2")
# Questão 2
function = '((sin(x)*cos(x))/((1/1.25)-cos(x)^2))-tan(80/2)'
a = '0'
b = '60'
error = '0.009'
secante(float(a), float(b), float(error), function)
