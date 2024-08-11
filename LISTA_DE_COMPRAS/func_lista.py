import molde


def lista():

    nova_lista = list()
    nova_lista2 = list()
    with open('lista_compras.txt','r') as arquivo:
        for i in arquivo.readlines():
                nova_lista = i.split(';')
        for c in nova_lista: # abrir o arquivo,separar os ";" e 
                nova_lista2.append(c.split('-'))# "-" e acrescentar em uma nova lista
        nova_lista2.pop(len(nova_lista2)-1) # tirar o ultimo 
        
    return nova_lista2

def mostrar_visu():
    

    print('='*50)
    print(f'{'LISTAS DOS PRODUTOS':^50}')
    print('='*50)

    print(f'{'ID':^5}|{'NOME':^15}|{'PREÇOS':^20}|')
    molde.traco()

    arquivo = open('lista_compras.txt','r')
 
# posso substituir pelo formato que fiz na função DEF REMOVER()

    for i in arquivo.readlines(): # [NOME: MACARRAO-PRECO: 23.00;NOME: ARROZ-PRECO: 44.00;NOME: SUCO-PRECO: 12.00;]
        
        nova_lista = i.split(';') # separei os ;[ 'NOME: MACARRAO-PRECO: 23.00','NOME: ARROZ-PRECO: 44.00','NOME: SUCO-PRECO: 12.00','']
        nova_lista.pop(len(nova_lista)-1) # precisei tirar o ultimo indice, pois sempre ficará vazio.
         
        for index,c in enumerate(nova_lista):
            nova_lista1 = c.split('-')# separei novamente - ['NOME: MACARRAO','PRECO: 23.00',...]
            nome_produto = nova_lista1[0].split(':') # separei somente o nome ['NOME','MACARRAO',...]
            preco_produto = nova_lista1[1].split(':') # separei somente o preco [...,'PRECO', '23.00',...]
            print(f'{index +1:^5}|{nome_produto[1]:^15}|  R$ {preco_produto[1]:^15}|')
           
        molde.traco()
        
    arquivo.close()
    
