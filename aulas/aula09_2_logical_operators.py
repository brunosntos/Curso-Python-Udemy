# AND, OR, NOT

# Valores considerados falsy = 0, 0.0, '', False, None

# Avaliação de curto circuito
print(True and 0.0 and 0)

print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))

print(0 or '123' or True or 0.0)

senha = input('Senha: ') or 'Sem senha'
print(senha)

valor = input('Valor: ')

if valor != '':
    print('não vazio')
else:
    print('vazio')