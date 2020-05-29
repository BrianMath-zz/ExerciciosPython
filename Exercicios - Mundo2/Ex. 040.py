# Ex. 040
n1 = float(input("Digite a n1: "))
n2 = float(input("Digite a n2: "))
med = (n1+n2)/2

if med < 5.0:
	print(f"REPROVADO com média {med:.1f}!!!")
elif (med >= 5.0) and (med < 7.0):
	print(f"RECUPERAÇÃO com média {med:.1f}!!")
else:
	print(f"APROVADO com média {med:.1f}!")
