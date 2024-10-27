import random

cpf_gerado = ''

for _ in range(9):
    cpf_gerado += str(random.randint(0,9))

nove_digitos = []

for i in range(9):
    nove_digitos.append(int(cpf_gerado[i]))

contagem_regressiva = range(10,1,-1)

conta_digito = 0

for i, digito in enumerate(nove_digitos):
    conta_digito += digito * contagem_regressiva[i] 

conta_digito %= 11

primeiro_digito = 0 if conta_digito < 2 else 11 - conta_digito

dez_digitos = []

for i in nove_digitos:
    dez_digitos.append(i)

dez_digitos.append(primeiro_digito)

contagem_regressiva = range(11,1,-1)
conta_digito = 0

for i, digito in enumerate(dez_digitos):
    conta_digito += digito * contagem_regressiva[i]

conta_digito %= 11

segundo_digito = 0 if conta_digito < 2 else 11 - conta_digito

cpf_completo = ''

for digito in dez_digitos:
    cpf_completo += str(digito)

cpf_completo += str(segundo_digito)

print(cpf_completo)

