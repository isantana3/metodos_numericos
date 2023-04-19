from utils.in_out_workers import TxtWorker


def calculate_absolute_variation(previous_matrix: list, actual_matrix: list):
    response_matrix = []
    for actual, previous in zip(actual_matrix, previous_matrix):
        response_matrix.append(abs(actual - previous))
    return response_matrix


def calculate_variations(previous_matrix: list, actual_matrix: list):
    absolute_variation = calculate_absolute_variation(previous_matrix, actual_matrix)
    return absolute_variation


def solved_the_problem(absolut_variation: list, error: float):
    for response in absolut_variation:
        if response > error:
            return False
    return True


def jacobi(base_matrix: list, error: float):
    maximum_iterations = 0
    previous_solution = []
    actual_solution = []
    absolute_variation = []
    for row in base_matrix:
        actual_solution.append(0)
        previous_solution.append(0)
        absolute_variation.append(error + 1)
    while not solved_the_problem(absolute_variation, error):
        for i in range(len(base_matrix)):
            matrix = base_matrix[i].copy()
            matrix[i], matrix[-1] = matrix[-1], matrix[i]
            x = 0
            for j in range(len(row) - 1):
                if i == j:
                    x += matrix[j]
                else:
                    x = x - (matrix[j] * previous_solution[j])
            x /= matrix[-1]
            previous_solution[i], actual_solution[i] = actual_solution[i], x

        absolute_variation = calculate_variations(previous_solution, actual_solution)
        maximum_iterations += 1
        if maximum_iterations > 30:
            break
    print(maximum_iterations)
    return actual_solution


def converge(base_matrix: list):
    element = 0
    for i in range(len(base_matrix)):
        sum_row = 0
        sum_column = 0
        for j in range(len(base_matrix)):
            if i == j:
                element = base_matrix[i][j]
            else:
                sum_row += abs(base_matrix[i][j])
                sum_column += abs(base_matrix[j][i])
        if element < sum_column or element < sum_row:
            return False
    return True


def run():
    data: TxtWorker = TxtWorker('jacobi.txt')
    data.read_matrix()
    answers = []
    for i in range(len(data.matrix)):
        if converge(data.matrix[i]):
            answers.append(jacobi(data.matrix[i], data.error[i]))
        else:
            answers.append(['does not converge'] * len(data.matrix[i]))

    data.write_matrix(answers)


run()
