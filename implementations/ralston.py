from utils.in_out_workers import TxtWorkerV3
import math


def steps(h, interval):
    return round(((float(interval[1]) - float(interval[0])) / h), 0)


def solve_function(f, x, y):
    function = f.replace(' x', str(x)).replace('y', str(y))
    return eval(function)


def ralston(x, y0, f, h, intervalo):
    answers = []
    answers.append(str(0) + ': ' + str(round(y0, 3)))
    for i in range(int(steps(h, intervalo))):
        k1 = solve_function(f, x, y0)
        k2 = solve_function(f, x + h, y0 + k1 * h)
        y0 = y0 + ((2 / 3) * k1 + (2 / 3) * k2) * h
        x = x + h
        answers.append(str(i * h) + ': ' + str(round(y0, 3)))
    return answers


def run():
    data: TxtWorkerV3 = TxtWorkerV3('ralston.txt')
    data.read()
    answers = []
    for i in range(len(data.y0)):
        answers.append(ralston(0, data.y0[i], data.f[i], data.h[i], data.interval[i]))

    data.write(answers)


run()
