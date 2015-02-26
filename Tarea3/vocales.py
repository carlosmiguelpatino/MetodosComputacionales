import sys as sys

n = int(sys.argv[1])
lineas = []


file = open("Sainte-Beuve.txt", "r")

for i in range(n):
	lineas.append(file.readline())

for i in range(len(lineas)):
	linea = lineas[i]
	print linea
	count = 0
	for j in range(len(linea)):
		letra = linea[j]
		if letra.isalnum() == True:
			if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
				count += 1
				
	print "El numero de vocales en la lineas", i, "es", count


