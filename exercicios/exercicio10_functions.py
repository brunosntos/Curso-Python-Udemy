def multiplicar(*args):
    total = 1

    for _ in args:
        total *= _

    return total

def impar_ou_par(numero):
    if numero % 2 == 0:
        return 'Par'
    
    return 'Ímpar'

numeros = 3,3,5
numeros_multiplicados = multiplicar(*numeros)
verificar_tupla = 'Sim' if type(numeros) is tuple else 'Não'

print(numeros_multiplicados)
print(impar_ou_par(numeros_multiplicados))
print(f'Números é uma tupla? {verificar_tupla}')
