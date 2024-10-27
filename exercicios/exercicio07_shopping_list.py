import os

shopping_list = []

while True:
    os.system('cls')

    print('OPÇÕES:')
    print('0. Encerrar o programa')
    print('1. Listar itens')
    print('2. Adicionar item na lista')
    print('3. Excluir item da lista')

    option = input('\nEscolha a opção desejada pelo índice: ')

    if option == '0':
        break

    elif option == '1':

        if not len(shopping_list) == 0:
            print('\nListando todos os itens')

            for i, item in enumerate(shopping_list):
                print(f'{i}. {item}')
        else:
            print('\nA lista está vazia.')

        input('\n[ENTER] para continuar.')

    elif option == '2':

        for i, item in enumerate(shopping_list):
            print(f'{i}. {item}')

        new_item = input('\nDigite o nome do novo item a ser adicionado na lista: ')

        if new_item == '':
            input('Não pode adicionar um item vazio. [ENTER]')
            continue
        else:
            shopping_list.append(new_item)
            input(f'O item ({new_item}) foi adicionado na lista. [ENTER]')
            continue
        
    elif option == '3':

        for i, item in enumerate(shopping_list):
            print(f'{i}. {item}')

        try:
            index_del = int(input('\nDigite o índice da lista para ser apagado: '))

            try:
                item_removed = shopping_list.pop(index_del)

                input(f'\nO item ({item_removed}) foi removido da lista. [ENTER]')
            except IndexError:
                input(f'\nEsse índice não existe ({index_del}). [ENTER]')
                continue


        except ValueError:
            input('Você não digitou um valor válido. [ENTER]')

    else:
        input('\nVocê não digitou uma opção válida. [ENTER]')
        continue

if len(shopping_list) == 0:
    print('\nVocê não tem itens na lista\n')
else:
    print('\nSua lista de itens: ')
    
    for i, item in enumerate(shopping_list):
        print(f'{i}. {item}')