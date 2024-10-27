"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
import sys
import os

print('Exercício 1')
numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero = int(numero)
else:
    sys.exit('Você não digitou um inteiro.')

if numero % 2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')

input('ENTER para continuar...')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

os.system('cls')
print('Exercício 2')
try:
    horas = int(input('Que horas são? '))

    bom_dia = (0 <= horas <= 11)
    boa_tarde = (12 <= horas <= 17)
    boa_noite = (18 <= horas <= 23)

    if bom_dia:
        print('Bom dia')
    elif boa_tarde:
        print('Boa tarde')
    elif boa_noite:
        print('Boa noite')

except ValueError:
    sys.exit('Você não digitou um valor válido.')

input('ENTER para continuar...')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

os.system('cls')
print('Exercício 3')

nome = input('Digite seu nome: ')
nome_curto = len(nome) <= 4

if nome_curto:
    print(f'Seu nome é curto pois possui somente {len(nome)} letras.')
else:
    print(f'Seu nome é longo pois possui {len(nome)} letras.')

input('ENTER para continuar...')