import sqlite3
import os

class Banco_dados:
    def __init__(self):
        
        self.banco = sqlite3.connect("lista_Compras")
        self.curso = self.banco.cursor()

    def criar_Banco(self):

        try:
            self.curso.execute("""
                            CREATE TABLE IF NOT EXISTS lista(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        preco REAL NOT NULL)
                        """)

            self.banco.commit()
            self.banco.close
        except:
            print("Ocorreu um erro ao inciar o banco de dados")
        else:
            print("Banco de dados criado com sucesso!")

    def adicionar_no_banco(self,nome,preco):
        self.curso.execute("""
                            INSERT INTO lista (nome , preco)
                           VALUES   (?,?)
                           """,(nome,preco))
        self.banco.commit()
        self.banco.close()

    def extrair_todos_dados(self):
        self.curso.execute("SELECT * FROM lista")   
        usuarios = self.curso.fetchall() # retornar todos os produtos.
        usuarios = [usuario for usuario in usuarios if usuario is not None]
        """
        for usuario in usuarios -> Itera sobre casa elemento usuario da lista usuarios
        if usuario is not None  -> Apenas adicina usuario à nova lista se ele não for None.
            [usuario...]        -> Cria uma nova lista contendo apenas os elementos filtrados.
        """
        return usuarios
    
    def remover_dados(self,id,nome,delet =False):            

            if delet == True:
                for i in id:              
                    self.curso.execute("DELETE FROM lista WHERE id = (?)",(i))
                    self.banco.commit()

                for i in nome:
                    self.curso.execute("DELETE FROM lista WHERE nome = (?)",(i))
                    self.banco.commit()
            
                self.curso.execute("""
                                CREATE TABLE temp_table AS SELECT * FROM lista ORDER BY id
                                """)
                self.banco.commit()
                

                self.curso.execute("DROP TABLE lista")
                self.banco.commit()

                self.curso.execute("""
                                CREATE TABLE IF NOT EXISTS lista(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            preco REAL NOT NULL)
                            """)

                self.banco.commit()

                self.curso.execute("INSERT INTO lista (nome,preco) SELECT nome,preco FROM temp_table")
                self.banco.commit()

                self.curso.execute("DROP TABLE temp_table")

