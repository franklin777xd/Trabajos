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
		print("ok. si")
		print("nel. no")

def numero():	
	x = True
	numero = int(input("ingrese valor"))
	while x == True:
		numero = numero + 1
		print(numero)
		if numero == 100 and 200 and 300 and 400 and 500 and 600 and 700 and 800 and 900 and 1000:
			x = False
	pregunta()

numero()