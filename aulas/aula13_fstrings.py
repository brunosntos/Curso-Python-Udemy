# Pads (espaços)

variavel = 'gaita'

print(f'{variavel: >20}.')
print(f'{variavel: <20}.')
print(f'{variavel: ^20}.')

print('')
print('-' * 21)
print('')

print(f'{variavel:0>20}.')
print(f'{variavel:X<20}.')
print(f'{variavel:Z^20}.')

print('')
print('-' * 21)
print('')

print(f'Hexadecimal de 13.000: {13000:08X}')