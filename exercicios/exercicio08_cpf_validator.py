import sys

cpf_enviado_usuario = input('Digite o seu CPF (somente números): ')

if not (cpf_enviado_usuario.isdigit()) or (len(cpf_enviado_usuario) != 11):
    sys.exit('\nDados inseridos incorretos. Não utilize pontos ou traços, e informe os 11 digitos do CPF.\n')

digitos_repetidos = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)

if digitos_repetidos:
    sys.exit('\nCPF inválido.\n')

cpf_enviado_usuario_format = ''

for i, digito in enumerate(cpf_enviado_usuario):
    cpf_enviado_usuario_format += digito

    if i == 2:
        cpf_enviado_usuario_format += '.'
    if i == 5:
        cpf_enviado_usuario_format += '.'
    if i == 8:
        cpf_enviado_usuario_format += '-'

nove_digitos = []

for i in range(9):
    nove_digitos.append(int(cpf_enviado_usuario[i]))

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

cpf_completo_format = ''

cpf_completo_format += cpf_completo[:3] + '.' + cpf_completo[3: 6] + '.' + cpf_completo[6: 9] + '-' + cpf_completo[9:12]

print(f'\nO primeiro verificador desse CPF é {primeiro_digito}')
print(f'O segundo verificador desse CPF é {segundo_digito}')

print(f'\nCPF completo: {cpf_completo_format}')

if cpf_completo == cpf_enviado_usuario:
    print('\nO CPF enviado é válido.\n')
else:
    print('\nO CPF enviado não é válido.\n')
