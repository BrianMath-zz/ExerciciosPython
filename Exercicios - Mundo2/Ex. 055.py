# Ex. 055

""" Versão 1

massMa, massMe = 0, 9999

for i in range(1, 6):
	mass = float(input(f"Digite a massa (kg) da pessoa {i}: "))
	if massMa < mass:
		massMa = mass
	elif massMe > mass:
		massMe = mass

print(f"Maior massa: {massMa} kg")
print(f"Menor massa: {massMe} kg")"""

massas = []

for i in range(1, 6):
	massas.append(float(input(f"Digite a massa (kg) da pessoa {i}: ")))

print(f"Maior massa: {max(massas)} kg")
print(f"Menor massa: {min(massas)} kg")
