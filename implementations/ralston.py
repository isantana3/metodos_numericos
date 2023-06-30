from utils.in_out_workers import TxtWorker


def steps(h, interval):
    return round(((float(interval[1]) - float(interval[0])) / h), 0)


def calculate(f, x, y):
    expression = f.split('x')
    expression = str(x).join(expression)
    expression = expression.split('y')
    expression = str(y).join(expression)
    return eval(expression)


def ralston(x, y0, f, h, intervalo):
    y = []
    for i in range(int(steps(h, intervalo))):
        k1 = calculate(f, x, y0)
        k2 = calculate(f, x + h, y0 + k1 * h)
        yh = y0 + ((2 / 3) * k1 + (2 / 3) * k2) * h
        y0 = yh
        x = x + h
        y.append(str(i) + ': ' + str(round(yh, 3)))
    return y


def run():
    data: TxtWorker = TxtWorker('ralston.txt')
    data.read_euler()
    answers = []
    for i in range(len(data.a)):
        answers.append(
            ralston(0, data.a[i], data.funcao[i], data.b[i], data.interval[i])
        )

    data.write_euler(answers)


run()
