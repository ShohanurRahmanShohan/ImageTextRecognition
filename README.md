# Image to Text 

A Flask application for extracting text from images using Tesseract OCR. Supports both Bangla and English languages.

## Features

- Upload images for text extraction using Tesseract OCR.
- Supports text recognition in Bangla and English.
- Processes images in-memory.

## Prerequisites

- Python 3.x
- Flask
- pytesseract
- Tesseract OCR with Bangla language data

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/FlaskTextExtractor.git
    cd FlaskTextExtractor
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Install Tesseract OCR and Bangla language data:
    - On Ubuntu/Debian:
      ```sh
      sudo apt-get install tesseract-ocr tesseract-ocr-ben
      ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Access the app at `http://0.0.0.0:5000` or `http://<your-ip-address>:5000`.

