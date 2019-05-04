def numero():
	x = True
	numero = int(input("ingrese valor"))
	while x == True:
		numero = numero + 1
		print(numero)
		if numero == 100:
			x = False
	pregunta()

def pregunta():
		print("------------------------------------------")
		print("Desea seguir ejecutando")
		print("1. si")
		print("2. no")
numero()