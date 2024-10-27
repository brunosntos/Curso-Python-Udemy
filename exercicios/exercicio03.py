nome = 'Bruno Santos'
novo_nome = ''

for i in range(len(nome)):
    novo_nome += f'*{nome[i]}'

novo_nome += '*'
print(novo_nome)