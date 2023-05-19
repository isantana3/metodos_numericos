from utils.in_out_workers import TxtWorker


def mmq(x, y):
    u0 = [1] * len(x)
    u1 = x
    lengh = len(x)

    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_xx = sum(valor**2 for valor in x)
    sum_u0 = sum(u0)
    sum_u1 = sum(u1)

    a = (lengh * sum_xy - sum_x * sum_y) / (sum_xx * lengh - sum_x**2)
    b = (sum_xx * sum_y - sum_xy * sum_x) / (sum_xx * lengh - sum_x**2)

    return b, a


def run():
    data: TxtWorker = TxtWorker('mmq_discreet.txt')
    data.read_2d_points()
    answers = []
    for i in range(len(data.point_x)):
        answers.append(mmq(data.point_x[i], data.point_y[i]))

    data.write_2d_points(answers)


run()
