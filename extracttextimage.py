import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Muhammad Ammar\AppData\Local\Programs\Tesseract-OCR\tesseract'
print(pytesseract.image_to_string(r'C:\Users\Muhammad Ammar\Pictures\Capture.PNG'))