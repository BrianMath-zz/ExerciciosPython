# Ex. 058
from random import choice

PC = choice(range(1, 11))
palp, vez = 11, 0

print("Vou pensar em um número entre 1 e 10")
print("Tente descobrir!\n")

while palp != PC:
	palp = int(input("Em qual número eu pensei? "))
	vez += 1

print(f"\nVocê acertou com {vez} tentativa(s)!")
