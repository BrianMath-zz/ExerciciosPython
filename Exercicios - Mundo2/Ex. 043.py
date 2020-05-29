# Ex. 043
massa = float(input("Digite sua massa (kg): "))
alt = float(input("Digite sua altura (m): "))
imc = massa/(alt**2)

print(f"\nSeu IMC é de {imc:.1f}")
if imc < 18.5:
	print("Você está ABAIXO DO PESO! Cuidado!")
elif imc < 25:
	print("Você está com o PESO IDEAL. Parabéns")
elif imc < 30:
	print("Você está SOBREPESO!")
elif imc < 40:
	print("Você está com OBESIDADE!")
else:
	print("Você está com OBESIDADE MÓRBIDA! Cuidado!")
