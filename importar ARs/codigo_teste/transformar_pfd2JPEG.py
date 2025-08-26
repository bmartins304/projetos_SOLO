import os
from pdf2image import convert_from_path

pdf_path= r"codigo_teste\ars juntas.pdf"
out_folder = "pfds_transformados_em_JEPG"
dpi = 150
fmt = 'jpeg'

os.makedirs(out_folder,exist_ok=True)

imagens = convert_from_path(pdf_path,dpi=dpi,fmt=fmt,poppler_path=r"venv\Include\bin\Tesseract-OCR\poppler-24.08.0\Library\bin")

for i, image in enumerate(imagens):
    image.save(f"{out_folder}/pagina_{i + 1}.jpg","JPEG")
    print(f"pagina {i + 1} salva com sucesso")

print("conversão concluida")

