Algoritmo TALLER_ALGORITMOS
	Escribir "Distancia entre vehículos (km)"
	Leer d
	Escribir "Velocidad vehículo 1 (km/h)"
	Leer v1
	Escribir "Velocidad vehículo 2 (km/h)"
	Leer v2
	Si v1>v2 Entonces
		t <- d/v1
	SiNo
		t<- d/v2
	Fin Si
	Escribir "Tiempo (min): " t*60
FinAlgoritmo
