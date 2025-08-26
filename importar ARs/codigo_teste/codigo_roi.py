import cv2
import pytesseract
import numpy
img= cv2.imread('pfds_transformados_em_JEPG\pagina_2.jpg')

cv2.imshow('Documento',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

caminho= r"venv\Include\bin\Tesseract-OCR"

x,y=100,50
w,h=400,80

roi = img[y:y+h,x:x+w]

gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
_, binary_roi = cv2.threshold(gray_roi,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto_roi = pytesseract.image_to_string(binary_roi, lang='por', config='--psm 6')
print("Texto na ROI:", texto_roi)