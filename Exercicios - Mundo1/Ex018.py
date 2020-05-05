#Ex. 018
from math import cos, sin, tan, radians
ang = int(input("Digite um ângulo: "))
ang_rad = radians(ang)
print(f"Seno de {ang}°: {sin(ang_rad):.2f}")
print(f"Cosseno de {ang}°: {cos(ang_rad):.2f}")
print(f"Tangente de {ang}°: {tan(ang_rad):.2f}")
