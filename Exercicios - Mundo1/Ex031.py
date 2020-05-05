#Ex. 031
dist = int(input("Qual a distância da sua viagem? "))
if dist <= 200:
    print(f"Sua passagem custará R${dist*0.5:.2f}")
else:
    print(f"Sua passagem custará R${dist*0.45:.2f}")