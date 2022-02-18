# Grupo














# EJERCICIO 7
Un profesor planea organizar un viaje escolar. El coste del viaje depende de la cantidad de alumnos participantes. Nos piden establecer el algoritmo de cálculo del precio de coste por alumno y del coste global del viaje en función de la cantidad de alumnos.
```
Algoritmo viaje_escolar

Entrada:
  numero_alumnos: ENTERO
  numero_dias: ENTERO
  coste_alojamiento: REAL
  precio_alumno: REAL
  coste_alumno: REAL
  coste_comida: REAL
  coste_total: REAL

Realización:
  coste_comida = 3,50 * numero_dias
  precio_alumno: 
    si numero_alumnos > 25: 61,00
    si numero_alumnos <= 25: 67,30
    fin si
  coste_alojamiento:
    si numero_alumnos < 30: 4,75 * numero_dias
    si numero_alumnos >= 30 y numero_alumnos <= 35: 4,00 * numero_dias
    si numero_alumnos > 35: 3,50 * numero_dias
    fin si
  coste_alumno = precio_alumno + coste_comida + coste_alojamiento
  coste_total = coste_alumno * numero_alumnos
Poscondición:
  Mostrar coste_alumno y coste_total
```






# EJERCICIO 8
A final de año, la empresa LA CAMPANA paga una prima anual a sus empleados camioneros. Escribir el algoritmo de cálculo de la prima anual que se concederá la empresa a cada conductor.
```

Algoritmo prima_anual
#Importe de la prima anual en función del número de accidentes, de la distancia
#recorrida y de la antigüedad del conductor.

Entrada
	accidentes : ENTERO # Número de accidentes
	distancia : ENTERO # Distancia recorrida
	Antigüedad : ENTERO # Antigüedad
	
Resultado: REAL

Variable
	prima_antigüedad:REAL
	prima_distancia:REAL
	
Realización
	si
		accidentes > 3
	entonces
		Resultado ← 0,00
	si no 
		#Calculo de la prima de antigüedad
		si
			antigüedad < 4
		entonces 
			prima_antigüedad ← 200,00 + REAL(antigüedad - 4)x20,00
		fin si
		#Cálculo de la prima de rendimiento
		prima_distancia ← inf (REAL(distancia)x0,01,REAL(400))
		#Cálculo de la prima anual
		Resultado ← (prima_antigüedad + prima_distancia)/REAL(accidentes + 1)
	fin si
	
Postcondición
  Mostrar resultado
...
 
    
