import pdf2image
import PyPDF2
import pytesseract
import cv2
from time import sleep

import re

'''
A class transformar_jpg ficará responsavel por abrir as paginas do arquivo e verifica os padroes para encontrar os protocolos
que serão enviados para a classe interface.

'''


class C_padrao_protocolo:

    def __init__(self):
        self.lista_arquivos_pdf = list()
        self.lista_1_protocolos_nao_format = list()
        self.lista_protocolo = list()
        self.lista_arquivo_n_ar = list()
        self.lista_pagina_sem_ar = list()


    def ler_arquivo(self,arquivo):

        self.lista_arquivos_pdf = arquivo
        '''
        # Se arquivo for uma string (caminho único), converta para lista
        if isinstance(arquivo, str):
            self.lista_arquivos_pdf.append(arquivo)
        else:  # Se já for uma lista de arquivos
            self.lista_arquivos_pdf.extend(arquivo)
        '''
        for i,Ars in enumerate(self.lista_arquivos_pdf):                # pegar cada arquivo
            self.lista_pagina_sem_ar = list()
            padrao =[r'CARTA',r'RECEBIMENTOS']                          #padroes que as Ars podem ter.
            
            '''
             # ler a imagem
            imagem = cv2.imread(Ars)
            caminho= r"venv\Include\bin\Tesseract-OCR"
             #pedir pro tesseract extrair o texto da imagem
            gray = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 3)
            _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
            pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
            texto = pytesseract.image_to_string(binary , lang="por")
            print(texto)
            padroes_protocolo = [
                r'(?i)protocolo[\s:-]*(\d{5,})',
                r'Protocolo:\s*(\d+)',
                r'Prot\.?\s*(\d+)',
                r'\b\d{5,}\b'
            ]
            for padrao in padroes_protocolo:
                correspondencias = re.findall(padrao,texto)
                if correspondencias:
                    return correspondencias[0]
            return "Numero de protocolo não encontrado"
       
            '''

            leitor = PyPDF2.PdfReader(Ars)                              #ler cada arquivo(Ars)
            for index,pagina in enumerate(leitor.pages):                #pegar cada pagina do arquivo selecionado(Ars)
                var_verificacao = 0                                     #veriavel para detequição de pagina com protocolo ou não
                prot_n_encontrado_arquivo = True                        #verificação se nesse arquivo tem pagina sem protocolo
                texto=pagina.extract_text().split("\n")  #yield               #extração dos textos da pagina
                #print(texto)
                for indece , letras in enumerate(texto):                #pegar cada texto extraido e verifica se tem o padrão
                    for padrao_i in padrao:                             #abrir a lista de padroes e verifica cada um           
                        check = re.findall(padrao_i,letras)             # iguala se foi encontrado o padrão
                        if check:                                       # se encontrar
                            self.lista_1_protocolos_nao_format.append(texto[indece])#adicionar na lista a string com o padrão
                            prot_n_encontrado_arquivo = False           # tonar a veriavel Falsa, já que foi encontrado
                            var_verificacao = 1                        # tornar a variavel 1, já que nessa pagina tem protocolo
                            break

                self.lista_pagina_sem_ar.append(var_verificacao)        #adiciona a lista os numeros 0 e 1: 1 quando tem protocolos e 0 quando não encontra
            if prot_n_encontrado_arquivo:                               # se  prot_n_encontrado_arquivo continuar True, adicionar essa pagina que não tem ars com protocolos
                self.lista_arquivo_n_ar.append(i)                       # pegar o indice desse arquivo adiciona na lista
                self.lista_arquivo_n_ar.append(self.lista_pagina_sem_ar.copy())#pegar  os 0 e 1 acrecentar logo em seguida, marcando qual pagina desse arquivo tem ou não protocolos

        #print(self.lista_1_protocolos_nao_format)
        return self.lista_1_protocolos_nao_format,self.lista_arquivo_n_ar  #retonar  as listas para as outras funções.


    '''
        função responsavel por pegar somente os protocolos encontrados nos padroes da função ler_arquivo
    
    '''
    def pegar_prot(self,arquivo):
            
            lista_para_format = arquivo                                 #pegar, como parametro , a lista self.lista_1_protocolos_nao_format 
            
            padrao2 = [r'\b\d{7}\b',r'\d{7}']                           #padrão para encontrar os protocolos
            
            for prot in lista_para_format:                              #pegar cada padrão da lista lista_para_format
                for check_doble in padrao2:                             #pegar os padrões para o protocolo
                    check2 = re.findall(check_doble,prot)               #verifica cada padrão para encontrar o protocolo
                    if check2:                                          # se encontrar
                        primeira_check = check2[0]                      # pegar o primeira acusação
                        self.lista_protocolo.append(primeira_check)     #adiciona na lista 
                        break                                           #encerra o loop
                
            return self.lista_protocolo                                 # retornar a lista com os protocolos somente.
                
                            
                
        
        