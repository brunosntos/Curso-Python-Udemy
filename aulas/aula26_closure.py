def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = saudacao('Bom dia')

print(falar_bom_dia('Bruno'))