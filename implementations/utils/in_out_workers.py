class TxtWorker:
    '''
    Read and write on txt files. Uses specific format of
    read and write for every single numeric method.
    '''

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.funcao = []
        self.a = []
        self.b = []
        self.error = []
        self.matrix = []
        self.legend = []
        self.point_x = []
        self.point_y = []
        self.n1 = []
        self.n2 = []

    def read_function(self):
        '''
        Read an file on path "methodos_numericos/inputs/".
        File must be on format:\n
        function F(x)\n
        a\n
        b\n
        error\n
        '''
        with open(f'inputs/{self.file_name}', 'r') as f:
            while True:
                function_line = f.readline()
                if not function_line:
                    break
                self.funcao.append(function_line)
                a_line = f.readline()
                self.a.append(float(a_line))
                b_line = f.readline()
                self.b.append(float(b_line))
                error_line = f.readline()
                try:
                    self.error.append(float(error_line))
                except:
                    pass

    def write_function_solution(self, output: list):
        '''Write output file on path "methodos_numericos/outputs/".'''
        with open(f'outputs/{self.file_name}', 'w') as f:
            for answer in output:
                f.write(f'{answer["function"]} :{answer["solution"]}\n')

    def read_newton_raphson(self):
        '''
        Read an file on path "methodos_numericos/inputs/".
        File must be on format:\n
        function F(x)\n
        x1\n
        error\n
        '''
        with open(f'inputs/{self.file_name}', 'r') as f:
            while True:
                function_line = f.readline()
                if not function_line:
                    break
                self.funcao.append(function_line)
                x1_line = f.readline()
                self.a.append(float(x1_line))
                error_line = f.readline()
                self.error.append(float(error_line))

    def read_matrix(self):
        '''
        Read an file on path "methodos_numericos/inputs/".
        File must be on format:\n
        linear_expression ~ ax+by+cz... = k\n
        .
        .
        .
        linear_expression ~ ax+by+cz... = k\n
        error (Optional)\n
        '''
        with open(f'inputs/{self.file_name}', 'r') as f:
            matrix = []
            while True:
                line = f.readline()
                if not line:
                    break
                if len(line) < 3:
                    continue
                if '=' not in line:
                    self.error.append(float(line))
                    continue
                row = []
                r_legend = []
                buffer = ''
                for char in line:
                    if char in '0123456789.-+':
                        buffer += char
                    elif char.isalpha() or char == '\n':
                        if char not in self.legend:
                            r_legend.append(char)
                        row.append(float(buffer))
                        buffer = ''
                    elif char == ',':
                        buffer += '.'
                matrix.append(row)
                if len(matrix) == len(row) - 1:
                    self.legend.append(r_legend)
                    self.matrix.append(matrix)
                    matrix = []
                    r_legend = []

    def write_matrix(self, output: list):
        '''Write output file on path "methodos_numericos/outputs/".'''
        with open(f'outputs/{self.file_name}', 'w') as f:
            for i in range(len(output)):
                for j in range(len(output[i])):
                    f.write(f'{self.legend[i][j]} = {output[i][j]}\n')
                f.write('\n')

    def read_2d_points(self):
        with open(f'inputs/{self.file_name}', 'r') as f:
            x = []
            y = []
            while True:
                point = f.readline()
                if not point and len(x) == 0:
                    break
                if len(point) > 3:
                    x.append(float(point.split(' ')[0]))
                    y.append(float(point.split(' ')[1]))
                else:
                    self.point_x.append(x)
                    self.point_y.append(y)
                    x = []
                    y = []

    def write_2d_points(self, output: list):
        with open(f'outputs/{self.file_name}', 'w') as f:
            for point in output:
                f.write(f'y = {point[0]} + {point[1]}X\n')

    def write_polynomials(self, output: list):
        with open(f'outputs/{self.file_name}', 'w') as f:
            for answer in output:
                print(answer)
                response = f'{answer[0]:.5f} '
                for i in range(1, len(answer)):
                    if answer[i] > 0:
                        response += '+ '
                    else:
                        response += '- '
                    response += f'{answer[0]:.5f}x^{i} '
                f.write(f'f{i}(x) = {response}\n')

    def write_lines(self, output: list):
        with open(f'outputs/{self.file_name}', 'w') as f:
            for line in output:
                f.write(line + '\n')

    def write_derivation(self, output: list):
        with open(f'outputs/{self.file_name}', 'w') as f:
            i = 0
            for derivations in output:
                f.write(f'{self.funcao[i]}')
                f.write(f'    1ª retardada: {derivations[0][0]}\n')
                f.write(f'    1ª centrada: {derivations[0][1]}\n')
                f.write(f'    1ª progressiva: {derivations[0][2]}\n')
                f.write(f'    2ª ordem: {derivations[1]}\n\n')

    def read_integration(self):
        '''
        Read an file on path "methodos_numericos/inputs/".
        The n1 and n2 are optional, if don't wanna pass then, input a newline
        File must be on format:\n
        function F(x)\n
        a\n
        b\n
        n1\n
        n2\n
        '''
        with open(f'inputs/{self.file_name}', 'r') as f:
            while True:
                function_line = f.readline()
                if not function_line:
                    break
                self.funcao.append(function_line)
                a_line = f.readline()
                self.a.append(float(a_line))
                b_line = f.readline()
                self.b.append(float(b_line))
                try:
                    n1_line = f.readline()
                    self.n1.append(int(n1_line))
                except:
                    self.n1.append(2)
                try:
                    n2_line = f.readline()
                    self.n2.append(int(n2_line))
                except:
                    self.n2.append(4)
                    continue
