numero=1
multiplicador=1

for numero in range (1,6):
    print(20*'-')
    print(f'Tabuada do {numero}')
    print(20*'-')
    for multiplicador in range (1,11):
        print(f'{numero} x {multiplicador} = {numero*multiplicador}')
