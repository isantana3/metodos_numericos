from utils.in_out_workers import TxtWorkerV3
import math


def steps(h, interval):
    return round(((float(interval[1]) - float(interval[0])) / h), 0)


def solve_function(f, x, y):
    function = f.replace(' x', str(x)).replace('y', str(y))
    return eval(function)


def euler_modified(x, y0, function, h, interval):
    answers = []
    total_steps = int(steps(h, interval))
    answers.append(str(0) + ': ' + str(round(y0, 3)))
    for i in range(total_steps):
        k1 = solve_function(function, x, y0)
        k2 = solve_function(function, x + h, y0 + k1 * h)
        y0 = y0 + (k1 + k2) * (h / 2)
        x = x + h
        answers.append(str(i * h) + ': ' + str(round(y0, 3)))

    return answers


def run():
    data: TxtWorkerV3 = TxtWorkerV3('euler_modified.txt')
    data.read()
    answers = []
    for i in range(len(data.y0)):
        answers.append(
            euler_modified(0, data.y0[i], data.f[i], data.h[i], data.interval[i])
        )

    data.write(answers)


run()
