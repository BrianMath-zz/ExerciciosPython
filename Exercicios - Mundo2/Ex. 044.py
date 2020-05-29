# Ex. 044
print("≈"*19)
print("Vendinha do Brian")
print("≈"*19)
print("")

preco = float(input("Digite o preço do produto: R$"))
print("-"*32)
print("Condições de pagamento:")
print("[1] À vista em dinheiro/cheque")
print("[2] À vista no cartão")
print("[3] Em 2x no cartão")
print("[4] Em 3x ou mais no cartão")
fPagamento = int(input("\nComo vai pagar? "))

# Condição de pagamento 1
if fPagamento == 1:
	print("\n*À vista em dinheiro/cheque*")
	preco = preco-(preco*0.1)
	print("Com essa forma de pagamento você recebeu 10% de desconto!!!")
	print(f"Seu produto custará R${preco:.2f}")

# Condição de pagamento 2
elif fPagamento == 2:
	print("\n*À vista no cartão*")
	preco = preco-(preco*0.05)
	print("Com essa forma de pagamento você recebeu 5% de desconto!!!")
	print(f"Seu produto custará R${preco:.2f}")

# Condição de pagamento 3
elif fPagamento == 3:
	print("\n*Em 2x no cartão*")
	preco = preco/2
	print("Com essa forma de pagamento você pagará em 2x sem juros!!!")
	print(f"Seu produto custará 2x de R${preco:.2f}")

# Condição de pagamento 4
elif fPagamento == 4:
	print("\n*Em 3x ou mais no cartão*")
	nParcelas = int(input("Deseja pagar em quantas parcelas? "))
	preco = (preco+(preco*0.2)) / nParcelas
	print(f"Com essa forma de pagamento você pagará em {nParcelas}x com 20% de juros!!!")
	print(f"Seu produto custará {nParcelas}x de R${preco:.2f}")

print("_"*32)
print("\nObrigado pela preferência!")
print("Tenha um bom dia e volte sempre!")
