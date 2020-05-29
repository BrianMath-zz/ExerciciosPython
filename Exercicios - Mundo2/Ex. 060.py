# Ex. 060
num = int(input("Digite um número inteiro: "))
c = fat = num

if num == 0:
	print("0! = 1")
else:
	while c > 1:
		c -= 1
		fat *= c
	print(f"{num}! = {fat}")

"""# Usando módulo de matemática
from math import factorial

num = int(input("Digite um número inteiro: "))

print(f"O fatorial de {num} é {factorial(num)}")"""
