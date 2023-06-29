from utils.in_out_workers import TxtWorker


def steps(h, interval):
    aux = (float(interval[1]) - float(interval[0])) / h
    return round(aux, 0)


def calculate(f, x, y):
    expression = f.split('x')
    expression = str(x).join(expression)
    expression = expression.split('y')
    expression = str(y).join(expression)
    return eval(expression)


def euler(x, y0, f, h, interval):
    y = []
    for i in range(int(steps(h, interval))):
        yh = y0 + calculate(f, x, y0) * h
        y0 = yh
        x = x + h
        y.append(str(i) + ': ' + str(round(yh, 3)))
    return y


# arq=open('euler.txt','r')
# final=open('eulerf.txt', 'w')

# while 1:
#     interval=[]
#     a = arq.readline()
#     if not a:
#         break
#     while a!='\n':
#         interval.append(a)
#         a = arq.readline()
#     a=arq.readline()
#     while a!='\n':
#         if not a:
#             break
#         y0=a
#         a = arq.readline()
#         f=a
#         a = arq.readline()
#         h=a
#         a = arq.readline()

#     g=euler(0,float(y0),f,float(h), interval)

#     final.write(str(g)+'\n\n')
# arq.close
# final.close


def run():
    data: TxtWorker = TxtWorker('euler.txt')
    data.read_euler()
    answers = []
    for i in range(len(data.a)):
        answers.append(euler(0, data.a[i], data.funcao[i], data.b[i], data.interval[i]))

    data.write_euler(answers)


run()
