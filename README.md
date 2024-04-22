# Prerequisites
## Install Tesseract
### MacOS
`brew install tesseract`
### Windows 
Download the installer from the official Tesseract at UB Mannheim repository (https://github.com/UB-Mannheim/tesseract/wiki).
Run the installer and follow the instructions. Make sure to note the installation path (e.g., C:\Program Files\Tesseract-OCR).
Add the Tesseract installation path to your system`s PATH environment variable so that it can be accessed from the command line.

### Linux
```
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```

# Setup
```
python -m venv venv  # Create a virtual environment (optional)
source venv/bin/activate  # Activate virtual environment (Linux/macOS)
venv\Scripts\activate  # Activate virtual environment (Windows)

pip install -r requirements.txt
```
