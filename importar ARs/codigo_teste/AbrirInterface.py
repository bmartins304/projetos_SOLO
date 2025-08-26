from tkinter import Tk,filedialog


def selecionar_arquivo():
    root=Tk()
    root.withdraw() # essconder janela

    caminho_arquivo = filedialog.askopenfilenames(
        title="selecinar um arquivo",
        filetypes=(
            ("todos os arquivos","*.*"),
            ("arquivos pdf","*.pdf")
        )
    )
    lista_arquivo = list(caminho_arquivo)


    if caminho_arquivo:
        print("arquivo selecionado:")
        for arquivo in lista_arquivo:
            print(arquivo)
        return caminho_arquivo  
    else:
        print("nenhum arquivo seleciando")
        return None
    
arquivo = selecionar_arquivo()