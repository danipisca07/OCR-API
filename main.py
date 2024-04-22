from flask import Flask, request, jsonify
import io
from PIL import Image
from utils.process_image import process_image 

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        try:
            # Read the file from the request as bytes in memory
            image_bytes = file.read()
            # Open the image directly from the bytes
            image = Image.open(io.BytesIO(image_bytes))
            
            # Process the image using your OCR function
            results = process_image(image)
            return jsonify(results)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "File upload failed"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
