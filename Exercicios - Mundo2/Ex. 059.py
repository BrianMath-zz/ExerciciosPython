# Ex. 059
while True:
	print("-"*26)
	n1 = float(input(" Digite um número: "))
	n2 = float(input(" Digite mais um número: "))

	while True:
		print("\n[1] Somar")
		print("[2] Multiplicar")
		print("[3] Maior")
		print("[4] Novos números")
		print("[5] Sair do programa")
		option = int(input("O que deseja fazer? "))

		# Caso 1
		if option == 1:
			print(f"\n{n1} + {n2} = {n1+n2}")
			print("-"*16)

		# Caso 2
		elif option == 2:
			print(f"\n{n1} x {n2} = {n1*n2}")
			print("-"*16)

		# Caso 3
		elif option == 3:
			print(f"\nMaior número: {max(n1, n2)}")
			print("-"*16)

		# Caso 4 ou 5
		elif option == 4 or option == 5:
			break

		# Casos diferentes
		else:
			print("\nOpção inválida. Digite novamente!")
			print("-"*33)

	# Caso 5
	if option == 5:
		break

print("\nPrograma finalizado com sucesso!")
