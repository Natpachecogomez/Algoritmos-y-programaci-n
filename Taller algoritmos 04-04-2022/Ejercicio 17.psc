Algoritmo TALLER_ALGORITMOS
	Escribir "Distancia entre vehÝculos (km)"
	Leer d
	Escribir "Velocidad vehÝculo 1 (km/h)"
	Leer v1
	Escribir "Velocidad vehÝculo 2 (km/h)"
	Leer v2
	Si v1>v2 Entonces
		t <- d/v1
	SiNo
		t<- d/v2
	Fin Si
	Escribir "Tiempo (min): " t*60
FinAlgoritmo
