def mru ():
	x = True
	while x == True:

		velocidad= input("ingrese la velocidad")
		distancia= input("ingrese la distancia")
		tiempo= input("ingrese el tiempo")
		if velocidad == "":
			velocidad = 0
			velocidad = int(velocidad)
			distancia = int(distancia)
			tiempo = int(tiempo)
			v=distancia/tiempo
			print("La velocidad es"+str(v))
			print("desea seguir ejcutando")
			print("1.Si")
			print("2.No")
			opcion = int(input())
			if opcion==1:
				x = True
			elif opcion >= 2:
				x = False
		elif distancia == "":
			velocidad = float(velocidad)
			distancia = 0
			distancia = float(distancia)
			tiempo = float(tiempo)
			d=velocidad*tiempo
			print("La distancia"+str(d))
			print("desea seguir ejcutando")
			print("1.Si")
			print("2.No")
			opcion = int(input())
			if opcion==1:
				x = True
			elif opcion >= 2:
				x = False
		elif tiempo == "":
			velocidad = float(velocidad)
			distancia = float(distancia)
			tiempo = 0
			tiempo = float(tiempo)
			t=distancia/velocidad
			print("el tiempo es "+str(t))
			print("desea seguir ejcutando")
			print("1.Si")
			print("2.No")
			opcion = int(input())
			if opcion==1:
				x = True
			elif opcion >= 2:
				x = False
		elif velocidad and distancia == "":
			x = True
		elif velocidad and tiempo == "":
			x= True
	
mru()



