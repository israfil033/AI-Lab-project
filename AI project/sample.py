import pytesseract
from PIL import Image
im = Image.open("C:/Users/Esha/Desktop/AI PROJECT/AI project/frame.png")
pytesseract.pytesseract.tesseract_cmd = 'C:/Users/Esha/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/tesseract'
text = pytesseract.image_to_string(im, lang = 'eng')
print(text)
