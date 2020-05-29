# Ex. 054
from datetime import date

maior = menor = 0

for i in range(1, 8):
	nasc = int(input(f"Digite o ano de nascimento da pessoa {i}: "))
	if date.today().year - nasc >= 21:
		maior += 1
	else:
		menor += 1

print(f"Maiores de idade: {maior}")
print(f"Menores de idade: {menor}")
