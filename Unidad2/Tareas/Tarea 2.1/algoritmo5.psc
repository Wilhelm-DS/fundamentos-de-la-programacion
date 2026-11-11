Algoritmo Algoritmo5
	Leer A
	Si A>100 Entonces
		Ti <- 20
	SiNo
		Si A<=100 Y A>=50 Entonces
			Ti <- 35
		SiNo
			Si A<=20 Y A<=49 Entonces
				Ti <- 40
			SiNo
				Si A<20 Entonces
					Ti <- 70
				FinSi
			FinSi
		FinSi
	FinSi
	Tt <- A*Ti
	Escribir 'El costo individual es de ', Ti, '. ', 'El costo total es de ', Tt, '.'
FinAlgoritmo
