import ADICIOANR_LISTA
import	editar
import arquivo
from molde import *
import os
from time import sleep
import relatorio
import func_lista

arq = 'lista_compras.txt'
opcao = ('Adicionar o produto','mostrar lista','remover produto','relatório','Sair')

while True:

    #verificar a existencia do arquivo
    if not arquivo.existe_arquivo():
        arquivo.criar_arquivo(arq)
    #Fim verificar a existencia do arquivo

    #menu de opções
    molde_menu()   
    for indice,escolha in enumerate(opcao):
        print(f'{ indice+1:5} - {escolha}')
    traco()
    
    escolha_indice = int(input('Informe o número da ação que deseja: '))  
    #fim do menu de opção
    
    if escolha_indice > len(opcao) or escolha_indice < 1:
        print('informar somente os número indicados acima')
        sleep(2)
    else:
        os.system('cls') or None
        
        # escolha das opções
        if escolha_indice == 5:
            print('FLW,MAN!!!')
            break
        if escolha_indice == 1:
            ADICIOANR_LISTA.adicionar()
        if escolha_indice == 2:
            func_lista.mostrar_visu()
            ajustar_traco()
            sleep(2)
        if escolha_indice == 3:
            func_lista.mostrar_visu()
            editar.remover(input('ID do produto separando com ","(999 para VOLTAR): '))
        if escolha_indice == 4:
            relatorio.fazer_relatorio()









