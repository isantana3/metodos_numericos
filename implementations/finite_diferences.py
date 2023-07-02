from utils.in_out_workers import TxtWorkerV3


def steps(h, interval):
    return round(((float(interval[1]) - float(interval[0])) / h), 0)


def solve_function(f, x, y):
    function = f.replace('x', str(x)).replace('y', str(y))
    return eval(function)


def finite_differences(x, y, equation, step_size, interval):
    answers = []
    total_steps = int(steps(step_size, interval))
    answers.append(str(0) + ': ' + str(round(y, 3)))

    for i in range(1, total_steps + 1):
        y = y + step_size * solve_function(equation, x, y)
        x = x + step_size
        answers.append(str(i) + ': ' + str(round(y, 3)))

    return answers


def run():
    data: TxtWorkerV3 = TxtWorkerV3('finite_differences.txt')
    data.read()
    answers = []
    for i in range(len(data.y0)):
        answers.append(
            finite_differences(0, data.y0[i], data.f[i], data.h[i], data.interval[i])
        )

    data.write(answers)


run()
