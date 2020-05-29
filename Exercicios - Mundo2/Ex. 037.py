# Ex. 037
num = int(input("Digite um número inteiro: "))
print("-"*19)
print('''Bases de conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')

numConv = int(input("Para qual base deseja converter? "))
if numConv == 1:
	print(f"\n{num} em BINÁRIO é {bin(num)[2:]}")
elif numConv == 2:
	print(f"\n{num} em OCTAL é {oct(num)[2:]}")
elif numConv == 3:
	print(f"\n{num} em HEXADECIMAL é {hex(num)[2:]}")
else:
	print("\nOpção inválida! Tente novamente!")
