# Ex. 050
soma = 0

for i in range(1, 7):
	n = int(input(f"Digite o valor {i}: "))
	if n % 2 == 0:
		soma += n
print("A soma dos números pares digitados é", soma)
