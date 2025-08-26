#codigo para abrir a interface para pegar os arquivos em pdf usando TKinter
import armazenar_prots
import transformar_ler_pdf2jpeg
from tkinter import Tk,filedialog
import os
from pdf2image import convert_from_path
from fpdf import FPDF
import shutil
import fitz
'''
A classe interface tem como proposito abrir a seleção de arquivos.
Exclusivamente em pdf pesquisavel.

A função  criar_pastas_jpg fica responsavel por separar e salvar 
as ars em pastas diferente. Quando vericadas e não localizado os protocolos
ela criará outra pasta para guardar esse arquivo para o usuario verificar
com os proprios olhos.


'''
class Interface:
    
    def __init__(self):
        pass

    def selecionar_arquivo():
        root=Tk()
        root.withdraw()

        caminho_arquivo = filedialog.askopenfilenames(
            title="selecinar um arquivo",
            filetypes={
                ("arquivo PDF",".pdf"),
                ("arquivo JPG",".jpg")
            }
        )

        lista_arquivo = list(caminho_arquivo)

        return lista_arquivo

    def criar_pastas_jpg(pdfs,lista_arquivo_n_ar=None):
        proximo_numero = 1   
        proximo_numero_n_ar = 1 
        numero_anterior = 0
        numero_anterior_n_ar = 0
        lista_paginas = list()
        encontrado = False
        arquivos_pfd = pdfs
        arquivo_nao_ar = lista_arquivo_n_ar
        dpi=150
        folder="imagens_JPG"
        folder_2="Não_ARs"
        fmt='jpeg'
        
        os.makedirs(folder,exist_ok=True)
        '''
        def salvar_imagem_jpg(imagem):
            numero_anterior = 0
    
            imagens = convert_from_path(imagem,dpi=dpi,fmt=fmt,poppler_path=r"venv\Include\bin\Tesseract-OCR\poppler-24.08.0\Library\bin")

            for  imagen in (imagens):
                                numero_jpg = lambda x : x + numero_anterior
                                imagen.save(f"{folder}/pagina_{numero_jpg(proximo_numero)}.jpg","JPEG")
                                print(f'pagina {numero_jpg(proximo_numero)} salva com sucesso')
                                numero_anterior = numero_jpg(proximo_numero)
            
        '''           
        # criar a função para transfomar as paginas em jpg
        def trans_pdf_jpg_n_ar(imagen):

            nonlocal numero_anterior_n_ar
            nonlocal proximo_numero_n_ar

            numero_jpg = proximo_numero + numero_anterior_n_ar
            imagen.save(f"{folder_2}/pagina_{numero_jpg}.jpg","JPEG")
            print(f'pagina {numero_jpg} salva com sucesso')
            numero_anterior_n_ar = numero_jpg

        def trans_pdf_jpg(imagen):

            nonlocal numero_anterior
            nonlocal proximo_numero

            numero_jpg = proximo_numero + numero_anterior
            imagen.save(f"{folder}/pagina_{numero_jpg}.jpg","JPEG")
            print(f'pagina {numero_jpg} salva com sucesso')
            numero_anterior = numero_jpg


        
        # funlçao para verificar qual indice é o documento para separas as paginas e armazenar o numero da pagina que tem quer ser dividida
        def verificar_pagina(index):
            nonlocal lista_paginas
            nonlocal encontrado

            encontrado=False
           

            try:
                for i,p in enumerate(arquivo_nao_ar):
                        if not isinstance(p,list):
                            if p == index:
                               
                                lista_paginas = arquivo_nao_ar[i+1]
                                encontrado =  True
                        
            except IndexError:
                
                lista_paginas = arquivo_nao_ar[(index-1)+1]
                return True



        for indece,arquivos_com_ar in enumerate(arquivos_pfd):
            

            imagens = convert_from_path(arquivos_com_ar,dpi=dpi,fmt=fmt,poppler_path=r"venv\Include\bin\Tesseract-OCR\poppler-24.08.0\Library\bin")

            for index,imagen in enumerate(imagens):
                

                if not arquivo_nao_ar:
                                 
                    trans_pdf_jpg(imagen)

                else:
                    os.makedirs(folder_2,exist_ok=True)

                    if verificar_pagina(indece) or encontrado:
                        
                        if lista_paginas[index] == 0:
                            trans_pdf_jpg_n_ar(imagen)
                            

                        elif lista_paginas[index] == 1:
                            trans_pdf_jpg(imagen)
                            
                    else:
                        trans_pdf_jpg(imagen)                 
                    

arquivos = Interface.selecionar_arquivo()
numero_protocolo,arquivo_n_ar = transformar_ler_pdf2jpeg.C_padrao_protocolo().ler_arquivo(arquivos)
Interface.criar_pastas_jpg(arquivos,arquivo_n_ar)
numero_protocolo = transformar_ler_pdf2jpeg.C_padrao_protocolo().pegar_prot(numero_protocolo)
#armazenar_prots.criar_dataFrame(numero_protocolo).dataframe()
print("Numero de protocolo encontrado: ",numero_protocolo)

