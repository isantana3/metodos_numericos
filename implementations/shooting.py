from utils.in_out_workers import TxtWorker


def steps(h, interval):
    return round(((float(interval[1]) - float(interval[0])) / h), 0)


def calculate(f, x, y, z):
    aux = f.split('x')
    aux = str(x).join(aux)
    aux = aux.split('y')
    aux = str(y).join(aux)
    aux = aux.split('z')
    aux = str(z).join(aux)
    return eval(aux)


def rungekutta(interval, y0, z0, f, g, h):
    y = []
    y.append(y0)
    x = float(interval[0])
    for i in range(int(steps(h, interval))):
        k1 = h * calculate(f, x, y0, z0)
        l1 = h * calculate(g, x, y0, z0)
        k2 = h * calculate(f, x + (1 / 2) * h, y0 + (1 / 2) * k1, z0 + (1 / 2) * l1)
        l2 = h * calculate(g, x + (1 / 2) * h, y0 + (1 / 2) * k1, z0 + (1 / 2) * l1)
        k3 = h * calculate(f, x + (1 / 2) * h, y0 + (1 / 2) * k2, z0 + (1 / 2) * l2)
        l3 = h * calculate(g, x + (1 / 2) * h, y0 + (1 / 2) * k2, z0 + (1 / 2) * l2)
        k4 = h * calculate(f, x + h, y0 + k3, z0 + l3)
        l4 = h * calculate(g, x + h, y0 + k3, z0 + l3)
        yh = y0 + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        zh = z0 + (1 / 6) * (l1 + 2 * l2 + 2 * l3 + l4)
        x = x + h
        y0 = yh
        z0 = zh
        y.append(yh)

    return y


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
    data: TxtWorker = TxtWorker('shooting.txt')
    data.read_shooting()
    answers = []
    for i in range(len(data.a)):
        yh1 = rungekutta(
            data.interval[i],
            (data.a[i]),
            0,
            data.error[i],
            data.funcao[i],
            (data.legend[i]),
        )
        yh2 = rungekutta(
            data.interval[i], 0, 1, data.error[i], data.funcao[i], (data.legend[i])
        )
        answers.append(
            shooting(yh1, yh2, (data.b[i]), data.interval[i], (data.legend[i]))
        )
    data.write_euler(answers)


run()
