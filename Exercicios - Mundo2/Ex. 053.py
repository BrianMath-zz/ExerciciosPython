# Ex. 053
frase1 = str(input("Digite uma frase sem caracteres especiais: ")).strip().lower().replace(" ", "")
frase2 = frase1[::-1]

if frase1 == frase2:
	print("Sua frase é um palíndromo!")
else:
	print("Sua frase não é um palíndromo!")
