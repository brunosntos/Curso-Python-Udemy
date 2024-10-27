# função sem parâmetros e sem retorno

def funcao_simples():
    print('\nEssa é uma função simples.')
    print('Ela não possui retorno.')
    print('Ela não possui parâmetross.\n')

# função com parâmetros e com retorno

def funcao_detalhes(numero_um, numero_dois, numero_tres):
    print('\nEssa é uma função mais detalhada.')
    print('Ela possui parâmetros e retorno.')

    resultado = (numero_um + numero_dois) * numero_tres

    return resultado

# função com argumentos nomeados

def funcao_nomeada(valor_a, valor_b):
    print(f'\n{valor_a=}')
    print(f'{valor_b=}\n')

# função com valor padrão

def funcao_valor_padrao(a, b, c=None):
    if c is not None:
        return f'\n{a=}, {b=}, {c=} | soma = {a + b + c}\n'
    else:
        return f'\n{a=}, {b=} | soma = {a + b}\n'
    

print(funcao_simples())
print('-' * 20)

print(f'Resultado da função detalhada: {funcao_detalhes(2,6,8)}\n')
print('-' * 20)

funcao_nomeada(valor_b = 5, valor_a = 19)
print('-' * 20)

print(funcao_valor_padrao(1, 2, 100))
