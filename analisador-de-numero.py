soma_pares=0
soma_impares=0
contadora_impar=0
contadora_par=0

for numero in range(1,31):
    if numero%2==0:
        print(numero)
        contadora_par+=1
        soma_pares+=numero
        
        
    else:
        print(numero)
        contadora_impar+=1
        soma_impares+=numero


print(f"Quantidade de numeros pares {contadora_par}!")
print(f"Quantidade de numeros impares {contadora_impar}!")
print(f"Soma dos numeros pares {soma_pares}!")
print(f"Soma dos numeros impares {soma_impares}!")


