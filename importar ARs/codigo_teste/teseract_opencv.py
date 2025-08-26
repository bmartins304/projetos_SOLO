import pytesseract
import cv2

# ler a imagem
imagem = cv2.imread("codigo_teste\pagina_1.jpg")
caminho= r"venv\Include\bin\Tesseract-OCR"
#pedir pro tesseract extrair o texto da imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem , lang="por")

print(texto)