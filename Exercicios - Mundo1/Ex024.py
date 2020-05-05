#Ex. 024
city = str(input("Digite a cidade onde nasceu: ")).strip().lower().split()
if city[0]=="santo":
    print("Sua cidade começa com 'Santo'")
else:
    print("Sua cidade não começa com 'Santo'")
