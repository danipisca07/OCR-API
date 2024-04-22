from PIL import Image
from utils.process_image import process_image

image = Image.open("tabella_nutrizionale.jpg")
nutrients = process_image(image)

for nutrient, amount in nutrients.items():
    print(f"{nutrient}: {amount}g")