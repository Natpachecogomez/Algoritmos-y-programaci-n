Algoritmo TALLER_ALGORTIMOS
	Escribir "Sueldo"
	Leer Sueldo
	x=1;
	Mientras x<=3 Hacer
		Escribir "Venta " x
		Leer Venta
		x=x+1
		Suma <- Venta+Suma
	Fin Mientras
	Escribir "Total ventas: " Suma
	Comisi�n <- Suma*0.10
	Escribir "Comisi�n: " Comisi�n
	Escribir "Sueldo total: " Comisi�n+Sueldo
FinAlgoritmo
