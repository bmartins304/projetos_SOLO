def molde_menu():
    print('='*50)
    print(f'{'MENU':^50}')
    print('='*50)

def traco():
    print('-'*50)

def molde_adicionar():
    print('='*50)
    print(f'{'ADICIONAR PRODUTO':^50}')
    print('='*50)

def ajustar_traco():
    maior = 0
    import func_lista
    nome_produtos = list()
    lista= func_lista.lista()

    for i in lista:
       nome_produtos.append(i)
    for i in nome_produtos:
        if len(i[0]) >= maior:
            maior = len(i[0])
    
    return maior