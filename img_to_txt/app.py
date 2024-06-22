import os
from flask import Flask, request, render_template, redirect, url_for
from PIL import Image
import pytesseract
from io import BytesIO

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # Process the image and extract text
            image = Image.open(file)
            # Specify the languages for Tesseract (Bengali and English)
            text = pytesseract.image_to_string(image, lang='ben+eng')
            return render_template('index.html', text=text)
    return render_template('index.html', text='')

if __name__ == '__main__':
    # Replace '0.0.0.0' with your actual IP address if you want
    app.run(host='0.0.0.0', port=5000, debug=True)
