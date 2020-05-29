# Ex. 049
num = int(input("Digite o número cuja tabuada deseja ver: "))

for i in range(1, 11):
	print(f"{num} x {i:^2} = {num*i}")
