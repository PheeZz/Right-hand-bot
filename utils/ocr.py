from PIL import Image
import pytesseract
import cv2
import os


def ocr(image='data/temp_ocr.png'):
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255,
                         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 3)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(f'data/{filename}', gray)
    text = pytesseract.image_to_string(
        Image.open(f'data/{filename}'), lang='rus+eng')
    os.remove(f'data/{filename}')
    return text


print(ocr())

# # загрузить образ и преобразовать его в оттенки серого
# image = cv2.imread(image)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # проверьте, следует ли применять пороговое значение для предварительной обработки изображения

# if preprocess == "thresh":
#     gray = cv2.threshold(gray, 0, 255,
#                          cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# # если нужно медианное размытие, чтобы удалить шум
# elif preprocess == "blur":
#     gray = cv2.medianBlur(gray, 3)

# # сохраним временную картинку в оттенках серого, чтобы можно было применить к ней OCR

# filename = "{}.png".format(os.getpid())
# cv2.imwrite(filename, gray)
