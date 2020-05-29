# Ex. 036
vCasa = float(input("Digite o valor da casa: R$"))
sal = float(input("Digite o seu salário: R$"))
anos = int(input("Em quantos anos deseja pagar a casa? "))
prest = vCasa/(anos*12)

if prest > sal*0.3:
	print("\nInfelizmente seu empréstimo não foi aprovado! :-(")
else:
	print(f"\nA prestação mensal da casa é de R${prest:.2f}")
