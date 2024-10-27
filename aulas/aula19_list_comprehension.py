numeros = [1, 2, 3, 4, 5, 6, 7]

numeros_dobrados = [x*2 for x in numeros]

numeros_dobrados_se_par = [x*2 for x in numeros if x%2==0]

numeros_triplos_se_impar = [x*3 for x in numeros if x%2!=0]

print(f'Números: {numeros}')
print(f'Números dobrados: {numeros_dobrados}')
print(f'Pares dobrados: {numeros_dobrados_se_par}')
print(f'Ímpares triplicados: {numeros_triplos_se_impar}')