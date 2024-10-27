def saudacao(horario, nome):
    if horario == 1:
        return f'Bom dia, {nome}!'
    elif horario == 2:
        return f'Boa tarde, {nome}!'
    elif horario == 3:
        return f'Boa noite, {nome}!'
    

def executar_funcao(funcao, *args):
    return funcao(*args)

print(executar_funcao(saudacao, 1, 'Bruno'))
print(executar_funcao(saudacao, 3, 'Bia'))
print(executar_funcao(saudacao, 2, 'Yuri'))