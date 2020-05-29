# Ex. 057
sex = str(input("Digite seu sexo (F/M): ")).upper().strip()

while "F" != sex != "M":
	sex = str(input("Sexo inválido! Digite F ou M: ")).upper().strip()

print(f"\nSexo digitado: {sex}")
