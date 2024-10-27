lista = ['item 1', 'item 2', 'item 3']
lista_b = [1, 2, 3, 4, 5]

valor1, valor2, valor3 = lista

somente_valor1, *_ = lista_b

print(somente_valor1)
print(_)