Algoritmo TALLER_ALGORITMOS
	Escribir "N�mero de dos cifras"
	Leer a
	Mientras a<10 o a>99 Hacer
		Escribir "El n�mero tiene que ser de dos cifras"
		leer a
	Fin Mientras
	Escribir a MOD 10, trunc(a/10)
FinAlgoritmo
