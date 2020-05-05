#Ex. 028
from random import choice

print("-"*37)
print(" Vou pensar em um número entre 0 e 5")
print(" Tente adivinhar!")
print("-"*37)

numero = choice([0, 1, 2, 3, 4, 5])

for i in range(1, 3):
    adiv = int(input(f"\nPalpite {i}: "))
    if adiv == numero:
        print("Acertou, parabéns!")
        a = 1
        break
    else:
        print("Errou, que pena!")
        a = 0
    
if a == 0:
    print("\nO número que pensei foi:", numero)
