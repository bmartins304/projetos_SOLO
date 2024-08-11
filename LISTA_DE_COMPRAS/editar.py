import molde
import func_lista
import os
from time import sleep
   
def remover(*nome):
    lista_arquivada = func_lista.lista()
    if str(*nome) == '999':
         pass # voltar
    elif str(*nome) > str(len(lista_arquivada)):
         print('informar somente os indices na lista mostrada!!')    
    else:  
        lista_indices_escolhidos = list()
        
        lista_insercao_arquivo = list() #listas que serão usadas para armazenamento

        lista_volatio = [*nome]
        for i in lista_volatio: # armazenamento dos indices escolhidos pelo usuario
            lista_indices_escolhidos = i.split(',') # separar a virgulas
        lista_indices_escolhidos.sort(reverse=True)# ordenar de formar decrescente

        lista_volatio.clear()

        for i in lista_indices_escolhidos:
            for num,p in enumerate(lista_arquivada):# verificar os indices iguais
                if int(i) - 1 == num:
                    lista_arquivada.remove(lista_arquivada[num])# remover os indices selecionados

        lista_indices_escolhidos.clear()
            
        for elem in lista_arquivada:
                lista_insercao_arquivo.append('-'.join(elem))  # adicinar a lista alterada em outra lista(Porque dava erro)

        with open('lista_compras.txt','w') as arquivo:
                for c in lista_insercao_arquivo:
                    arquivo.write(f'{c};')       # substituir os dados dentro do arquivo pela nova lista.

        pontinhos = ('.','.','.')
        print('REMOVENDO',end='')
        for i in pontinhos:
            print(i,flush=True,end='')
            sleep(1) 
        sleep(1)
        os.system('cls') or None
        print('PRODUTO REMOVIDO DA LISTA')
        sleep(0.5)

  
            


    
