
def existe_arquivo():
    try:
        arq = open('lista_compras.txt','r')
        arq.close()
    except FileNotFoundError:
        #print('arquivo não encontrado')
        return False
    else:
        #print('arquivo já existente')
        return True

def criar_arquivo(nome):
    try:
        arq = open(nome,'w+')
        arq.close()
    except:
        print('houve um erro ao criar um arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

    
  