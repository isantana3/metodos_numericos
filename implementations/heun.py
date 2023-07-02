from utils.in_out_workers import TxtWorkerV3


def steps(h, interval):
    return round(((float(interval[1]) - float(interval[0])) / h), 0)


def solve_function(f, x, y):
    function = f.replace('x', str(x)).replace('y', str(y))
    return eval(function)


def heun(x, y0, f, h, interval):
    answers = []
    for i in range(int(steps(h, interval))):
        aux = y0 + solve_function(f, x, y0) * h
        y0 = y0 + ((solve_function(f, x, y0) + solve_function(f, x + h, aux)) / 2) * h
        x = x + h
        answers.append(str(i) + ': ' + str(round(y0, 3)))
    return answers


def run():
    data: TxtWorkerV3 = TxtWorkerV3('heun.txt')
    data.read()
    answers = []
    for i in range(len(data.y0)):
        answers.append(heun(0, data.y0[i], data.f[i], data.h[i], data.interval[i]))

    data.write(answers)


run()
