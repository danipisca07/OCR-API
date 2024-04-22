import re
import pytesseract
from utils.divide_until_below import divide_until_below

# Set the path to the tesseract executable if it's not in your PATH
# Uncomment and adjust the path below if necessary
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows example

def process_image(image):
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    # Output lines for review
    lines = text.split('\n')

    for line in lines:
        print(line)

    # Define a regular expression pattern to match lines with nutrient information
    pattern = r'(\w+.*?)\s*([\d,]+)g'

    known_nutrients = [
        "energia",
        "calorie",
        "saturi",
        "grassi",
        "carboidrati",
        "zuccheri",
        "fibre",
        "proteine",
        "sale"
    ]

    # Extract nutrient information
    nutrients = {}
    for line in lines:
        line = line.replace(" g "," ").replace("g "," ").replace(" g"," ")  # Normalize spacing around 'g'
        for nutrient in known_nutrients:
            # Create a dynamic pattern for each known nutrient
            # The \b word boundary ensures that we match the whole word and not a substring
            pattern = rf'\b{nutrient}\b\s*([\d,]+)'
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                # Replace comma with dot for decimal
                amount = match.group(1).replace(',', '.')
                if(amount.isnumeric()):
                    # We use the known nutrient from our array, ensuring consistency
                    nutrients[nutrient] = divide_until_below(float(amount), 100, 10)
                    print(f"{nutrient}: {amount}")
                    break  # Stop checking other nutrients if we've found a match

    return nutrients

    

