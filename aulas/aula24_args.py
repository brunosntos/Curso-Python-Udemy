def soma(*args):
    resultado = 0

    for _ in args:
        resultado += _
    
    return resultado

numeros = 10,15,20,25,30
numeros_2 = 13,105,8,80,55,20,32

print(f'Soma dos números (valores passados individualmente): {soma(1,2,3,4,5)}')
print(f'Soma dos números (valores de uma lista): {soma(*numeros)}')
print(f'Soma dos números (valores de uma lista; teste 2): {soma(*numeros_2)}')

numeros_3 = 1,2,5

print(*numeros_3)
