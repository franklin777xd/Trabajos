#funcnio para trabajer con paises y capitales
def paisescapitales ():
	#almacenamineto de datos 
	pcapitales = {}
	x = True
	conteo = 0
	while  x== True:
		pais = input("ingrese el nombre del pais")
		capital = input("ingrese su capital")
		pcapitales[pais] = capital
		print(pcapitales)
		print("desea seguir ejecutando")
		print("si")
		print("no")
		opcion =input()
		if opcion == "si":
			pass
		elif opcion == "no":
			x = False
			for y,m in pcapitales.items():
				conteo = conteo +1
				print(str(conteo)+" "+ y +" "+m)



paisescapitales()