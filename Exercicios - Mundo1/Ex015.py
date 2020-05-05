#Ex. 015
km = int(input("Quantos km percorridos? "))
dia = int(input("Por quantos dias você alugou o carro? "))
preco = (dia*60) + (km*0.15)
print(f"Você deverá pagar R${preco:.2f}")
