from utils.in_out_workers import TxtWorker

def linear_regression(x, y):
    lengh = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_exp_x = sum(valor ** 2 for valor in x)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    a1 = (lengh * sum_xy - sum_x * sum_y) / (lengh * sum_exp_x - sum_x ** 2)
    a0 = sum_y / lengh - a1 * (sum_x / lengh)

    return a0, a1
def run():
    data: TxtWorker = TxtWorker('regression.txt')
    data.read_2d_points()
    answers = []
    for i in range(len(data.point_x)):
        answers.append(
            linear_regression(data.point_x[i], data.point_y[i])
        )

    data.write_2d_points(answers)


run()

