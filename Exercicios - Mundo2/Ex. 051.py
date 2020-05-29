# Ex. 051
num1 = int(input("Digite o primeiro termo da progressão: "))
raz = int(input("Digite a razão da progressão: "))

print(num1)
for i in range(0, 9):
	print(num1+raz)
	num1 += raz
