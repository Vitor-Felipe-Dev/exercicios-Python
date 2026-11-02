contadora=0
numero=0
limite=int(input("Digite o limite da contagem: "))

for numero in range(1,limite+1):
    if numero%2==0:
        print(numero)

        contadora=contadora+1


print( f"tem {contadora} numero pares")
