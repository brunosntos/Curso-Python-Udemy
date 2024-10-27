import os

operacoes = ['1','2','3','4']

while True:
    resultado = 0

    print('0. Encerrar')
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')

    operacao = input('\nEscolha a operação desejada pelo índice: ')

    if operacao == '0':
        break
    
    if operacao not in operacoes:
        input('\nVocê não digitou uma operação válida. [ENTER]')
        os.system('cls')
        continue

    try:

        primeiro_numero = int(input('\nDigite o primeiro número: '))
        segundo_numero = int(input('Digite o segundo número: '))

    except ValueError:

        print('\nVocê não digitou um número válido.')

    match(operacao):
        case '1':
            resultado = primeiro_numero + segundo_numero
        case '2':
            resultado = primeiro_numero - segundo_numero
        case '3':
            resultado = primeiro_numero * segundo_numero
        case '4':
            resultado = primeiro_numero / segundo_numero
            resultado = round(resultado, 1)

    input(f'\nO resultado dessa operação é {resultado}  [ENTER]')
    os.system('cls')

print('\nPrograma encerrado.')