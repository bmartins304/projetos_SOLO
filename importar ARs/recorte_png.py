import cv2
import pytesseract


caminho= r"venv\Include\bin\Tesseract-OCR"
#carregar imagem
imagem = cv2.imread(r"C:\Users\Bruno\Desktop\PYTHON\importar ARs\imagens_JPG\pagina_1.jpg")

#define as coordenadas do canto superior direito (x1,y1,x2,y2)
altura,largura = imagem.shape[:2]


x1,y1= int(largura * 0.7),0
x2,y2= largura,int(altura *0.3)


imagem_marcada = imagem.copy()

cv2.rectangle(imagem_marcada,(x1,y1),(x2,y2),(0,0,255),2)


cv2.imwrite('imagem_marcada.jpg',imagem_marcada)

roi = imagem[y1:y2,x1:x2]

pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

texto = pytesseract.image_to_string(roi,lang='por')

print('texto extraido: ',texto)

print(altura,largura)