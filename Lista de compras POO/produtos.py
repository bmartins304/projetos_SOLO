from banco_dados_produtos import Banco_dados

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
        self.dados = Banco_dados()

    def adicionar_lista(self):#acessar o banco de dados para colocar os produtos e os preços
        self.dados.adicionar_no_banco(self.nome,self.preco)

class Lista(Produto):
    def __init__(self):       
        self.dados = Banco_dados()
        self.encontrado =False
        self.cor_ver = '\033[91m'
        self.cor_reset = '\033[0m'


    def criar_banco(self):# iniciar o banco de dados
        self.dados.criar_Banco()

    def  listar_Produtos(self):
        lista = self.dados.extrair_todos_dados()
        print(f"{'ID':^10} | {'NOME':^10} | {'PREÇO':^10} |") # MOSTRAR A LISTA CUSTOMIZADA
        print("----------------------------------------------------") 
        for i,l in enumerate(lista):
            print(f"{lista[i][0]:^10} | {str(lista[i][1]).upper():^10} | R$ {lista[i][2]:^10.2f} |")

    def remover(self,id,nome):
        """
        preciso fazer um modo para mostrar ao usuario quais ids não estão no banco de dados e qual nome não foi encontrado.
        """  
        verifica_ID_Nome = self.dados.extrair_todos_dados()
        lista_id_encontrado = []
        lista_id_n_encontrado = []

        lista_nome_encontrado = []
        lista_nome_n_encontrado = []
        
        

        if id != []:
            for i in id:
                while True:#posso talvez tirar esse WHILE, mas não quero.
                    self.encontrado = False
                    for index,v in enumerate(verifica_ID_Nome):
                        if int(i) == verifica_ID_Nome[index][0]:
                            if i not in lista_id_encontrado:
                                lista_id_encontrado.append(i)
                            self.encontrado = True
                            break
                    if self.encontrado == True:
                        break
                    elif self.encontrado == False:
                        lista_id_n_encontrado.append(i)
                        break
        if nome != []:
            for i in nome:
                while True:
                    self.encontrado = False
                    for index,v in enumerate(verifica_ID_Nome):
                        if i == str(verifica_ID_Nome[index][1]).upper():
                            if i not in lista_nome_encontrado:
                                lista_nome_encontrado.append(i)
                            self.encontrado = True
                            break
                    if self.encontrado == True:
                        break
                    elif self.encontrado == False:
                        lista_nome_n_encontrado.append(i)
                        break
    
        if lista_id_encontrado != []:
            print(f"IDs que serão deletadas {lista_id_encontrado}")
        if lista_id_n_encontrado != []:
            print(f"{self.cor_ver}ID não encontrado {lista_id_n_encontrado}{self.cor_reset}")
        if lista_nome_encontrado != []:
            print(f"NOMEs que serão deletadas {lista_nome_encontrado}")
        if lista_nome_n_encontrado != []:
            print(f"{self.cor_ver}NOME não encontrado {lista_nome_n_encontrado}{self.cor_reset}")


        lista_id_encontrado.clear()
        lista_id_n_encontrado.clear()
        lista_nome_encontrado.clear()
        lista_nome_n_encontrado.clear()

        resp = input("Deseja excluir os dados? ")
        if resp == 'sim' or 'SIM' or 'Y' or  'y':
            resp = True
        else:
            resp = False

        self.dados.remover_dados(lista_id_encontrado,lista_nome_encontrado,delet=resp)

        


        """
        self.dados.curso.execute("DELETE FROM lista WHERE nome = (,)",(nome))
        self.dados.curso.execute("DELETE FROM lista WHERE id = (?)"(id))
        """
        