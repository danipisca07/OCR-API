import pytesseract
from PIL import Image

# Set the path to the tesseract executable if it's not in your PATH
# Uncomment and adjust the path below if necessary
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows example

# Load an image from disk
image = Image.open("tabella_nutrizionale.jpg")

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(image)

print(text)
