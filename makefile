tests:
	python3 implementations/tests.py
	
all:
	make  linear_regression
	make  regula_falsi
	make  newton_raphson
	make  secante
	make  gauss
	make  lu
	make  jacobi
	make  gs
	make  inversao

linear_regression:
	python3 implementations/linear_regression.py

regula_falsi:
	python3 implementations/regula_falsi.py

newton_raphson:
	python3 implementations/newton_raphson.py

secante:
	python3 implementations/secante.py

gauss:
	python3 implementations/eliminacao_de_gauss.py

lu:
	python3 implementations/fatoracaoLU.py

jacobi:
	python3 implementations/jacobi.py

gs:
	python3 implementations/gauss_seidel.py

inversao:
	python3 implementations/inversao.py