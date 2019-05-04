"""def repetir():
	x = True
	numero = 0
	while x == True:
		Nombres = input("ingrese Nombres")
		print(Nombres)
		Numero = Numero + 1
		if numero == 10:
			x = False
repetir()"""
"""def listas():
	libreria=["lapicero","cuadernos","folders","hojas","cartulinas"]
		for x in libreria:
			print(x)
listas()"""
def diccionario():
	libreria={"lapicero":2,"cuaderno":4,"folders":1,"hojas":1,"cartulina":1}
	for x,y in libreria.items():
		print(x+str(y))
diccionario()