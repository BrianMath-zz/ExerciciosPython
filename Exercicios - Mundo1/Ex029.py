#Ex. 029
V = int(input("Digite a velocidade do carro: "))
if V > 80:
    print("\nExcesso de velocidade!!!")
    print(f"Você foi multado em R${(V-80)*7:.2f}")
else:
    print("\nDentro da velocidade permitida.")
    print("Tenha um bom dia!")