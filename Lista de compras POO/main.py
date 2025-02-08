from produtos import Produto
from produtos import Lista
from time import sleep

"""
    OBS: implementar a função de fazer mais de uma lista e customizar o nome da lista.
        - criar a função para colocar os traços
"""


class Main:
    def __init__(self,nome):
        self.lista_IDS = []
        self.lista_nome = []
        self.nome_menu = nome
        self.opcao = ("SAIR","ADICIONAR PRODUTOS","VISUALIZAR LISTA","REMOVER PRODUTO")
        self.verde = "\033[92m"
        self.reset = "\033[0m"
        self.produto_preco = Lista()

    def inicio_Sis(self):
         lista = Lista()
         lista.criar_banco()

    def menu(self):
        largura = 40 # ajuste a largura conforme necessário
        titulo  = f"{'BEM VINDO A LISTA DE ' + self.nome_menu:^10}".upper()
        print(titulo.center(largura,"-")) # OUTRO FORMATO PARA CENTRALIZAR O TEXTO NOS TRAÇOS

        print(f"{self.verde}escolha uma das opções abaixo:{self.reset}")
        for i,o in enumerate(self.opcao):   
            print(f"[{i + 1 }] - {o}")# escolha das epções
        n_escolha = int(input("> "))
        return n_escolha

    def menu_1(self):
            pontinhos = (".",".",".")
            print("SAINDO DO SISTEMA",end=" ")
            for i in pontinhos:
                 print(i,flush=True,end="")
                 
                 
    def menu_2(self):#colocar os itens na classe pruduto.
        lista = Produto(input("Informe o nome do produto: "), float(input("Informe o preço: ")))
        lista.adicionar_lista()

    def menu_3(self):      
         self.produto_preco.listar_Produtos()#mostrar lista.

    def menu_4(self,*nome_ID):
        """
            não lembro como o eu do passado conseguiu fazer isso, mas o eu do futuro é incompetente.
        """
        lista_exlcluir = list()       
        lista_volatio = [*nome_ID]
        for i in lista_volatio:
             lista_exlcluir = i.split(',')
        for e in lista_exlcluir:
            try:       
                if int(e):#verifica se o valor inserido no input é numero ou string e depois separa.
                    self.lista_IDS.append(e)
            except ValueError:
                 self.lista_nome.append(e)
        self.produto_preco.remover(self.lista_IDS,self.lista_nome)
        

sistema = Main("teste")
sistema.inicio_Sis()
while True:
    n_e = sistema.menu()
    if n_e == 1:
        sistema.menu_1()
    elif n_e == 2:
         sistema.menu_2()
    elif n_e == 3:
         sistema.menu_3()
    elif n_e == 4:
        sistema.menu_3()
        sistema.menu_4(input("Escolha o ID e/ou NOME da item que deseja excluir(SEPARAR COM ,): ").upper())