try:
    numero = int(input('Digite um número inteiro: '))

    print(f'O número {numero} é par') if numero % 2 == 0 else print(f'O número {numero} é ímpar')

except ValueError:
    print('Você não digitou um número inteiro.')