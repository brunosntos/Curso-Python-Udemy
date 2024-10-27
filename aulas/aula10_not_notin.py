nome = 'luis'
print(nome)
print(f'3ª letra = {nome[2]}')
print(f'3ª letra (de trás pra frente) = {nome[-2]}')

letra = input('Digite uma letra para verificar se está no nome: ')

if letra in nome:
    print(f'A letra {letra} está no nome {nome}')
else:
    print(f'A letra {letra} não está no nome {nome}')

for i in nome:
    print(i)