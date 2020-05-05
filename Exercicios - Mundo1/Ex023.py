#Ex. 023
num = str(input("Digite um número: "))#.zfill(4) -> preenche com 0 até completar 4 casas
while len(num) < 4:
    num = "0" + num
print("Unidade: ", num[3])
print("Dezena: ", num[2])
print("Centena: ", num[1])
print("Unidade de milhar: ", num[0])
