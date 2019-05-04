def ingreso ():
	x = True
	while x == True:
		x = int(input("ingrese numero de tabla"))
		if x >= 0:
			tabla(x)
		pregunta = input("Desea seguir ejecutando? si/no")
		if pregunta == "si":
			x = True
		elif pregunta == "no":
			x = False

def tabla(x):
	y = True
	numero = 0
	while numero < 10:
		numero = numero + 1
		print(str(x)+" * "+str(numero)+" = "+str(x*numero))

ingreso()