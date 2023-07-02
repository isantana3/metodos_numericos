from utils.in_out_workers import TxtWorkerV3


def steps(h, interval):
    return round(((float(interval[1]) - float(interval[0])) / h), 0)


def solve_function(f, x, y, z):
    function = f.replace('x', str(x)).replace('y', str(y)).replace('z', str(z))
    return eval(function)


def rungekutta(interval, y0, z, f, g, h):
    answers = []
    answers.append(y0)
    x = float(interval[0])
    for i in range(int(steps(h, interval))):
        k1 = h * solve_function(f, x, y0, z)
        l1 = h * solve_function(g, x, y0, z)
        k2 = h * solve_function(f, x + (1 / 2) * h, y0 + (1 / 2) * k1, z + (1 / 2) * l1)
        l2 = h * solve_function(g, x + (1 / 2) * h, y0 + (1 / 2) * k1, z + (1 / 2) * l1)
        k3 = h * solve_function(f, x + (1 / 2) * h, y0 + (1 / 2) * k2, z + (1 / 2) * l2)
        l3 = h * solve_function(g, x + (1 / 2) * h, y0 + (1 / 2) * k2, z + (1 / 2) * l2)
        k4 = h * solve_function(f, x + h, y0 + k3, z + l3)
        l4 = h * solve_function(g, x + h, y0 + k3, z + l3)
        y0 = y0 + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        z = z + (1 / 6) * (l1 + 2 * l2 + 2 * l3 + l4)
        x = x + h
        answers.append(y0)

    return answers


def shooting(y1, y2, b, interval, h):
    y = []
    a = int(steps(h, interval))
    for i in range(a):
        y.append(
            str(i)
            + ': '
            + str(round((y1[i] + ((b - y1[a - 1]) / y2[a - 1]) * y2[i]), 3))
        )
    return y


def run():
    data: TxtWorkerV3 = TxtWorkerV3('shooting.txt')
    data.read_shooting()
    answers = []
    for i in range(len(data.y0)):
        yh1 = rungekutta(
            data.interval[i],
            (data.y0[i]),
            0,
            data.y[i],
            data.z[i],
            (data.h[i]),
        )
        yh2 = rungekutta(data.interval[i], 0, 1, data.y[i], data.z[i], (data.h[i]))
        answers.append(shooting(yh1, yh2, (data.y1[i]), data.interval[i], (data.h[i])))
    data.write(answers)


run()
