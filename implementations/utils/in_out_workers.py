class TxtWorkerV3:
    '''
    Specific implementation for 3rd relatory methods.
    Read and write on txt files. Uses specific format of
    read and write for every single numeric method.
    '''

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.y0 = []
        self.y = []
        self.y1 = []
        self.f = []
        self.h = []
        self.z = []
        self.interval = []

    def read(self):
        with open(f'inputs/{self.file_name}', 'r') as f:
            interval = []
            while 1:
                line = f.readline()
                if not line:
                    break
                while line != '\n':
                    interval.append(line)
                    line = f.readline()
                line = f.readline()
                while line != '\n':
                    if not line:
                        break
                    self.y0.append(float(line))
                    self.f.append(f.readline())
                    self.h.append(float(f.readline()))
                    line = f.readline()
                self.interval.append(interval)

    def read_shooting(self):
        with open(f'inputs/{self.file_name}', 'r') as f:
            while 1:
                interval = []
                a = f.readline()
                if not a:
                    break
                while a != '\n':
                    interval.append(a)
                    a = f.readline()
                a = f.readline()
                while a != '\n':
                    if not a:
                        break
                    self.y0.append(float(a))
                    self.y1.append(float(f.readline()))
                    self.y.append(f.readline())
                    self.z.append(f.readline())
                    self.h.append(float(f.readline()))
                    a = f.readline()
                self.interval.append(interval)

    def write(self, output: list):
        '''Write output file on path "methodos_numericos/outputs/".'''
        with open(f'outputs/{self.file_name}', 'w') as f:
            for answer in output:
                f.write(str(answer) + '\n\n')
