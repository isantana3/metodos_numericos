from utils.in_out_workers import TxtWorkerV3


def steps(h, interval):
    return round(((float(interval[1]) - float(interval[0])) / h), 0)


def solve_function(f, x, y):
    function = f.replace('x', str(x)).replace('y', str(y))
    return eval(function)


def rungekutta(x, y0, f, h, interval):
    answers = []
    for i in range(int(steps(h, interval))):
        k1 = solve_function(f, x, y0)
        k2 = solve_function(f, x + (1 / 2) * h, y0 + (1 / 2) * k1 * h)
        k3 = solve_function(f, x + (1 / 2) * h, y0 + (1 / 2) * k2 * h)
        k4 = solve_function(f, x + h, y0 + k3 * h)
        y0 = y0 + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4) * h
        x = x + h
        answers.append(str(i) + ': ' + str(round(y0, 3)))
    return answers


def run():
    data: TxtWorkerV3 = TxtWorkerV3('rungekutta.txt')
    data.read()
    answers = []
    for i in range(len(data.y0)):
        answers.append(
            rungekutta(0, data.y0[i], data.f[i], data.h[i], data.interval[i])
        )

    data.write(answers)


run()
