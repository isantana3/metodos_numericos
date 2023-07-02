all:
	make  euler
	make  euler_modified
	make  heun
	make  ralston
	make  rungekutta
	make  edo
	make  finite_diferences
	make  shooting

euler:
	python3 implementations/euler.py

euler_modified:
	python3 implementations/euler_modified.py

heun:
	python3 implementations/heun.py

ralston:
	python3 implementations/ralston.py

rungekutta:
	python3 implementations/runge_kutta_4th_order.py

edo:
	python3 implementations/edo_system.py

finite_diferences:
	python3 implementations/finite_diferences.py

shooting:
	python3 implementations/shooting.py
