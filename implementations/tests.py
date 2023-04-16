from bisseccao import bisseccao
import math


def test_bissection():
    function = 'x^4-2*x^3-4*x^2+4*x+4'
    a = -2.0
    b = -1.0
    error = 0.01
    max_interations = math.ceil(math.log2((b - a) / error))
    response = bisseccao(
        a=a,
        b=b,
        erro=error,
        function=function,
        max_interations=max_interations,
    )

    print('===========================================')
    if response['solution'] == 'X7 = -1.4140625':
        print('Bissecção: Pass')
    else:
        print('Bissecção: Fail')
        print('Expect: X7 = -1.4140625')
        print('Recieved: ' + response['solution'])
    print('===========================================')


test_bissection()
