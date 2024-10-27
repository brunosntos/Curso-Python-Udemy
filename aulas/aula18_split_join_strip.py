frase = '   Uma frase é formada    ,    por várias palavras,    teste.   '

separar_virgula = frase.split(',')

print(f'Frases sem correção: \n{separar_virgula}\n')

frases_corrigidas = []

for item in separar_virgula:
    frases_corrigidas.append(item.strip())

print(f'Frases corrigidas: \n{frases_corrigidas}\n')

frases_unificadas = ', '.join(frases_corrigidas)

print(f'Frases unificadas: \n{frases_unificadas}\n')
