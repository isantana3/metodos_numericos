tests:
	python3 implementations/tests.py
	
all:
	make  euler
	make  heun
	make  ralston
	make  rungekutta
	make  shooting
	make  lu
	make  jacobi
	make  gs
	make  inversao

euler:
	python3 implementations/euler.py

heun:
	python3 implementations/heun.py

ralston:
	python3 implementations/ralston.py

rungekutta:
	python3 implementations/runge_kutta_4th_order.py

shooting:
	python3 implementations/shooting.py

lu:
	python3 implementations/fatoracaoLU.py

jacobi:
	python3 implementations/jacobi.py

gs:
	python3 implementations/gauss_seidel.py

inversao:
	python3 implementations/inversao.py