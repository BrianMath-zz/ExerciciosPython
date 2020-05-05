#Ex. 035
l1 = int(input("Digite o lado 1 do triângulo: "))
l2 = int(input("Digite o lado 2 do triângulo: "))
l3 = int(input("Digite o lado 3 do triângulo: "))
if (l1<l2+l3) and (l2<l1+l3) and (l3<l1+l2):
    print("\nOs segmentos podem formar um triângulo!")
else:
    print("\nOs segmentos NÃO podem formar um triângulo!")
