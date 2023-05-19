from utils.in_out_workers import TxtWorker
import numpy as np


def mmq(x, y, m=2):
    n = len(x)
    A = np.zeros((n, m + 1))
    b = np.zeros(n)

    for i in range(n):
        for j in range(m + 1):
            A[i, j] = x[i] ** j
        b[i] = y[i]

    response = np.linalg.lstsq(A, b, rcond=None)[0]
    return response


def run():
    data: TxtWorker = TxtWorker('mmq_continuos.txt')
    data.read_2d_points()
    answers = []
    for i in range(len(data.point_x)):
        answers.append(mmq(data.point_x[i], data.point_y[i]))

    data.write_polynomials(answers)


run()
