#Ex. 022
nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome em maiúsculas é:", nome.upper())
print("Seu nome em minúsculas é:", nome.lower())
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras")
print(f"Seu 1º nome tem {nome.find(' ')} letras")
