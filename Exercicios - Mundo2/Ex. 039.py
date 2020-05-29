# Ex. 039
from datetime import date

anoNasc = int(input("Digite seu ano de nascimento: "))
resp = date.today().year - anoNasc

if resp < 18:
	print(f"Você precisará se alistar daqui a {18-resp} ano(s).")
elif resp == 18:
	print("Você precisa se alistar esse ano.")
else:
	print(f"Você precisava se alistar há {resp-18} ano(s)! Faça isso agora!")
