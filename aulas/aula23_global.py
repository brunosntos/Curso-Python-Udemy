soma = 0

def valores(x, y):
    global soma 
    soma = 10
    soma += x + y

    return soma
    
valores(10,20)

soma += 1

print(soma)
