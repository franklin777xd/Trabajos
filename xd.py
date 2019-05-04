#funcion para trabajar con paises y capitales
def paisescapitales ():
	#diccionario para almacenar paises y capitales
	paisescapitales = {}
	x = True
	conteo = 0
	while x == True:
		pais = input("ingrese nombre del pais")
		capital = input("ingrese su capital")
		paisescapitales[pais] = capital
		print(paisescapitales)
		respuesta = input("¿Desea seguir conociendo paises? si/no")
		if respuesta == "si":
			pass
		elif respuesta == "no":
			x = False
			for y,s in paisescapitales.items():
				conteo = conteo + 1
				print(str(conteo)+" "+ y + " " + s)

paisescapitales()