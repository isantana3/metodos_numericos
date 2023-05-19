tests:
	python3 implementations/tests.py
	
all:
	make  linear_regression
	make  mmq_discreet
	make  newton_dd
	make  lagrange
	make  mmq_continuos
	make  derivation
	make  simple_trap
	make  multi_trap
	make  simpson_13
	make  simpson_38

linear_regression:
	python3 implementations/linear_regression.py

mmq_discreet:
	python3 implementations/mmq_discreet.py

newton_dd:
	python3 implementations/newton_dd.py

lagrange:
	python3 implementations/lagrange_polynomials.py

mmq_continuos:
	python3 implementations/mmq_continuos.py

derivation:
	python3 implementations/numerical_derivation.py

simple_trap:
	python3 implementations/trapezoidal_integration.py

multi_trap:
	python3 implementations/trapezoidal_mult_integration.py

simpson_13:
	python3 implementations/simpson_1-3.py

simpson_38:
	python3 implementations/simpson_3-8.py

