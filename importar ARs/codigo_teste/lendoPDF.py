import PyPDF2


with open(r"codigo_teste\ars juntas.pdf",'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfReader(arquivo_pdf)

    for pagina in leitor.pages:
        texto=pagina.extract_text().split("\n")
        print(texto)


    




