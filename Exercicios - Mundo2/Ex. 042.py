# Ex. 042
l1 = int(input("Digite o lado 1: "))
l2 = int(input("Digite o lado 2: "))
l3 = int(input("Digite o lado 3: "))

if (l1 < l2+l3) and (l2 < l1+l3) and (l3 < l1+l2):
	print("\nEsses segmentos formam um triângulo!")
	if l1 == l2 == l3:
		print("3 lados iguais: triângulo EQUILÁTERO.")
	elif (l1 == l2 != l3) or (l1 == l3 != l2) or (l2 == l3 != l1):
		print("2 lados iguais: triângulo ISÓSCELES.")
	elif l1 != l2 != l3:
		print("Nenhum lado igual: triângulo ESCALENO.")
else:
	print("\nEsses segmentos NÃO formam um triângulo!")
