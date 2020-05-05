#Ex. 017
from math import hypot
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
print(f"A hipotenusa mede {hypot(co, ca):.2f}")
