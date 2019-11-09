from time import sleep

print('====== SPLASH CALCULATOR ======')
print('-------------------------------')
print('Olá')
print('-------------------------------')
while True:
    print('''
    Que valor será calculado?

        [ 1 ] Valor comum
        [ 2 ] Valor Reverso

    ''')
    perg = int(input('Qual operação deseja efetuar?\n: '))
    
    if perg == 1:
        base = float(input('Insira a base: '))
        height = float(input('Insira a altura: '))
        value = int(input('Insira o m²: '))
        price = base * height * value
        print(f'{price:.2f}')

    if perg == 2:
        base = float(input('Insira a base: '))
        height = float(input('Insira a altura: '))
        money = float(input('Insira o preço: '))
        reverse = money / (base * height)
        print(f'{reverse:.2f}')
    
    sleep(2)
    conf = str(input('Deseja continuar?\n: ')).upper()
    if conf == 'N':
        break


print('====== VOLTE SEMPRE! ======')