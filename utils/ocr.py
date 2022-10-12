from PIL import Image
import pytesseract
import cv2
import os


def ocr(image='data/temp_ocr.png'):
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255,
                         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    filename = f"{os.getpid()}.png"
    cv2.imwrite(f'data/{filename}', gray)
    text = pytesseract.image_to_string(
        Image.open(f'data/{filename}'), lang='rus')
    os.remove(f'data/{filename}')
    return text
