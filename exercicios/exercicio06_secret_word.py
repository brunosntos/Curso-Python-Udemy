import random
import os

palavras = ['python', 'programação', 'software', 'hardware', 'tecnologia', 'computador']

palavra = random.choice(palavras)

palavra_fragmentada = []
for letra in palavra:
    palavra_fragmentada.append(letra)

palavra_secreta_fragmentada = []
for i in range(len(palavra)):
    palavra_secreta_fragmentada.append('*')

palavra_secreta_formada = ''
for letra in palavra_secreta_fragmentada:
    palavra_secreta_formada += letra

tentativas = 0
while True:
    tentativas += 1
    print(f'\nTentativa {tentativas}:')
    print(f'\nPalavra secreta: {palavra_secreta_formada}')

    letra_tentativa = input('Digite uma letra: ').lower()

    for i ,letra in enumerate(palavra):
        if letra == letra_tentativa:
            palavra_secreta_fragmentada[i] = letra
    
    palavra_secreta_formada = ''

    for letra in palavra_secreta_fragmentada:
        palavra_secreta_formada += letra

    if '*' not in palavra_secreta_formada:
        break

os.system('cls')
print(f'\nVocê acertou! A palavra secreta era {palavra_secreta_formada}')
print(f'Número de tentativas: {tentativas}\n')