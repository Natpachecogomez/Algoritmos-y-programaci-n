Algoritmo TALLER_ALGORITMOS
	Escribir "Distancia entre veh�culos (km)"
	Leer d
	Escribir "Velocidad veh�culo 1 (km/h)"
	Leer v1
	Escribir "Velocidad veh�culo 2 (km/h)"
	Leer v2
	Si v1>v2 Entonces
		t <- d/v1
	SiNo
		t<- d/v2
	Fin Si
	Escribir "Tiempo (min): " t*60
FinAlgoritmo
