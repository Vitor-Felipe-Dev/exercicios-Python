#Verificador de nota

while True:
    try:
        nota_aluno=input('Digite a nota do aluno de 0 a 10:  ')
        nota=int(nota_aluno)

        if nota<0:
            print('Nota invalida!\n Digite uma nota positiva')
        elif nota>10:
            print('nota Invalida')
        else:
            if nota<7:
                print('Aluno de recuperação!')
            else:
                print('Aluno aprovado!')

            break
    except ValueError:
        print('Digite um  numero inteiro')
