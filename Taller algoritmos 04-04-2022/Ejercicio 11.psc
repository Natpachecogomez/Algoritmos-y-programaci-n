Algoritmo TALLER_ALGORITMOS
	x=1;
	Mientras x<=3 Hacer
		Escribir "Parcial " x
		Leer Parcial
		x=x+1
		Suma <- Parcial+Suma
	Fin Mientras
	Suma <- (Suma/3)*0.55
	Escribir "Porcentaje parciales: " Suma
	Escribir "Nota examen final"
	Leer ExFin
	ExFin <- ExFin*0.30
	Escribir "Porcentaje examen final: " ExFin
	Escribir "Nota trabajo final"
	Leer TraFin
	TraFin <- TraFin*0.15
	Escribir "Porcentaje trabajo final: " TraFin
	Escribir "Calificación final " Suma+ExFin+TraFin
FinAlgoritmo