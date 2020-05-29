# Ex. 048
impar = 0

for i in range(1, 501, 2):
	if i % 3 == 0:
		impar += i
print(f"A soma dos múltiplos ímpares de 3 entre 1 e 500 é {impar}")
