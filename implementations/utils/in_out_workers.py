class TxtWorker:
    '''Read and write on txt files. Uses specific format of
    read and write for every single numeric method.
    '''

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.funcao = []
        self.a = []
        self.b = []
        self.error = []

    def read_bissection(self):
        '''Read an file on path "methodos_numericos/inputs/".
        File must be on format:\n
        function F(x)\n
        a\n
        b\n
        error
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

    def write_bissection(self, output: list):
        '''Write output file on path "methodos_numericos/outputs/".'''
        with open(f'outputs/{self.file_name}', 'w') as f:
            for answer in output:
                f.write(f'{answer["function"]} :{answer["solution"]}\n')
