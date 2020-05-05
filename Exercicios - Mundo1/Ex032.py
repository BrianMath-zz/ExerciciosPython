#Ex. 032
from datetime import date
ano = int(input("Digite o ano que deseja verificar se é bissexto (0 para usar o ano atual): "))
if ano == 0:
    ano = date.today().year
    
if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            print(f"\n{ano} é um ano bissexto!")
        else:
            print(f"\n{ano} NÃO é um ano bissexto!")
    else:
        print(f"\n{ano} é um ano bissexto!")
else:
    print(f"\n{ano} NÃO é um ano bissexto!")
