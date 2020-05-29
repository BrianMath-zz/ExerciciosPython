# Ex. 041
from datetime import date
anoNasc = int(input("Digite seu ano de nascimento: "))
resp = date.today().year - anoNasc

if resp <= 9:
	print("Categoria: MIRIM.")
elif 14 >= resp > 9:
	print("Categoria: INFANTIL.")
elif 19 >= resp > 14:
	print("Categoria: JÚNIOR.")
elif 25 >= resp > 19:
	print("Categoria: SÊNIOR.")
else:
	print("Categoria: MÁSTER.")
