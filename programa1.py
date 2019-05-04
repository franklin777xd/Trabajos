def suma(cantx,canty):
	total = cantx+canty
	print(total)

def resta(cantx,canty):
	total = cantx-canty
	print(total)

def multiplicacion(cantx,canty):
	total = cantx*canty
	print(total)
	
def division(cantx,canty):
	total = cantx/canty
	print(total)

def ingreso():
	x = True
	while x == True:
		cantx = int(input("ingrese primer cantidad"))
		canty = int(input("ingrese segunda cantidad"))
		print("--------------------------------------------")
		print("Que opcion desea ejecutar")
		print("1. suma")
		print("2. resta")
		print("3. multilicacion")
		print("4. division")
		opcion = int(input("ingrese No. de opcion"))
		if opcion == 1:
			suma(cantx,canty)
		elif opcion == 2:
			resta(cantx,canty)
		elif opcion == 3:
			multiplicacion(cantx,canty)
		elif opcion == 4:
			division(cantx,canty)
			print("--------------------------------------------")
			print("desea seguir operando")
			print("1. si")
			print("2. no")
			desision = input("ingrese No. opcion")
			if desision == 1:
				x = True
			elif desision == 2:
				x = False

ingreso()