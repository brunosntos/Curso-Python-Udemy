# AND, OR, NOT

# Valores considerados falsy = 0, 0.0, '', False, None

login_salvo = 'usuário'
senha_salva = '12345'

login = input('Login: ')
senha = input('Senha: ')

if login == login_salvo and senha == senha_salva:
    print('Login realizado com sucesso.')
else:
    print('Login ou senha incorretos.')