#Ex. 026
nome = str(input("Digite uma frase: ")).strip().lower()
print("\nQuantidade de letras 'a':", nome.count("a"))
print("Posição da primeira letra 'a':", nome.find("a")+1)
print("Posição da última letra 'a':", nome.rfind("a")+1)
