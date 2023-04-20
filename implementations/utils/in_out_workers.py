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
                self.error.append(float(error_line))

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
