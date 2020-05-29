# Ex. 056
somaIdades, homemVelho, mulheresAbaixo20 = 0, 0, 0
nomeHomemVelho = ""

for i in range(1, 5):
	nome = input(f"\nDigite o nome da pessoa {i}: ")
	idade = int(input(f"Digite a idade da pessoa {i}: "))
	sexo = int(input(f"Digite o sexo (0-Homem, 1-Mulher) da pessoa {i}: "))

	# Soma das idades para fazer média
	somaIdades += idade

	# Nome do homem mais velho
	if (sexo == 0) and (homemVelho < idade):
		homemVelho = idade
		nomeHomemVelho = nome

	# Mulheres com menos de 20 anos
	if (sexo == 1) and (idade < 20):
		mulheresAbaixo20 += 1

print(f"\nMédia das idades: {somaIdades/4}")
print(f"Nome do homem mais velho: {nomeHomemVelho}")
print(f"Mulheres com menos de 20 anos: {mulheresAbaixo20}")
