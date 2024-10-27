letras_diferentes = []
letras_diferentes_quantidades = []
todas_as_letras = []

frase = 'O python é uma linguagem de programação multiparadigma.'\
        ' Python foi criado por Guido Van Rossum.'

for letra in frase:
    if (letra.lower() not in letras_diferentes) and letra.isalnum():
        letras_diferentes.append(letra.lower())

for letra in frase:
    if letra.isalnum():
        todas_as_letras.append(letra.lower())
    
for letra in letras_diferentes:
    contador = 0
    for _ in todas_as_letras:
        if letra == _:
            contador += 1
    
    letras_diferentes_quantidades.append(contador)

for valor1, valor2 in zip(letras_diferentes, letras_diferentes_quantidades):
    print(f'Letra {valor1}: {valor2} vezes')

letra_mais_rep_int = max(letras_diferentes_quantidades)
letra_mais_rep_ind = letras_diferentes_quantidades.index(letra_mais_rep_int)
letra_mais_rep_str = letras_diferentes[letra_mais_rep_ind]

print(f'\nA letra repetida mais vezes foi o "{letra_mais_rep_str}", aparecendo {letra_mais_rep_int} vezes.\n')


