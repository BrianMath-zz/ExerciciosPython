# Ex. 052
div = 0
num = int(input("Digite um número: "))

for i in range(1, num+1):
	if num % i == 0:
		div += 1
if div == 2:
	print(f"\n{num} É um número primo!")
else:
	print(f"\n{num} NÃO É um número primo!")
