#Verificador de idade

while True:
    try:
        idade=input('Digite sua idade: ')
        idade_int=int(idade)

        if idade_int<=0:
            print('Idade invalida!\n Digite uma idade positiva')
        elif idade_int>120:
            print('idade Invalida')
        else:
            if idade_int<=17:
                print('menor de idade!')
            else:
                print('Maior de idade!')

            break
    except ValueError:
        print('Digite um  numero inteiro')
