#Ex. 034
sal = float(input("Digite seu salário: R$"))
if sal <= 1250.0:
    print(f"O salário de R${sal:.2f} passa a ser de R${sal+(sal*0.15):.2f}")
else:
    print(f"O salário de R${sal:.2f} passa a ser de R${sal+(sal*0.1):.2f}")
