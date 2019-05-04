def paises ():
	listadopaises = []
	x = True
	conteo = 0
	conteoprint = 0
	while x == True:
		pais = input("ingresen nombre de paises ")
		listadopaises.insert(conteo,pais)
		conteo = conteo + 1
		print(conteo)
		print(listadopaises)
		print("desea seguir ejecutando ")
		print("1 si")
		print("2 no")
		opcion = input()
		if opcion == "si":
			pass
		elif opcion=="no":
			x = False
			for  y in listadopaises:
				conteoprint = conteoprint + 1
				print(str(conteoprint)+ " " + y)
paises()
