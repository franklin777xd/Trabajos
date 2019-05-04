def repetir():
	x = True
	while x == True:
		edad = int(input("ingrese edad"))
		print(edad)
		if edad>=18:
			print("Es mayor de edad")
			x = False
		else:
			print("Es menor de edad")
repetir():