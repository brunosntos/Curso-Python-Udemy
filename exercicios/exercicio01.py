import sys

name = input('Digite seu nome: ')
age = input('Digite sua idade: ')
letras = 0

if name == '' or age == '':
    sys.exit('Você deixou campos em branco.')

print(f'\nSeu nome é {name}')
print(f'Seu nome invertido é {name[::-1]}')
print(f'Sua idade é {age}')

if ' ' not in name:
    print('Seu nome não tem espaços')
else:
    print('Seu nome tem espaços')

for i in name:
    if i != ' ':
        letras += 1
print(f'Seu nome tem {letras} letras')

print(f'A primeira letra do seu nome é {name[0]}')
print(f'A última letra do seu nome é {name[len(name)-1]}')