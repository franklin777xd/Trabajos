def suma():
	cantidad1 = int(input("ingrese primer cantidad"))
	cantidad2 = int(input("ingrese segunda cantidad"))
	resultadosuma = cantidad1+cantidad2
	print(resultadosuma)
	multiplicacion()

def resta():
	cantidad1 = int(input("ingrese primer cantidad"))
	cantidad2 = int(input ("ingrese segunda cantidad"))
	resultadoresta = cantidad1-cantidad2
	print(resultadoresta)

def multiplicacion():
	cantidad1 = int(input("ingrese primer cantidad"))
	cantidad2 = int(input("ingrese segunda cantidad"))
	resultadomultiplicacion = cantidad1*cantidad2
	print(resultadomultiplicacion)
	resta()

def dvision():
	cantidad1 = int(input("ingrese primer cantidad"))
	cantidad2 = int(input("ingrese segunda cantidad"))
	resultadodivision = cantidad1/cantidad2
	print(resultadodivision)
	suma()

dvision()