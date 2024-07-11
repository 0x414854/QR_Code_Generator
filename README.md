![Static Badge](https://img.shields.io/badge/python-%233776ab?logo=python&logoColor=white)

# QR Code Generator

![github](https://github.com/0x414854/QR_Code_Generator/assets/128352715/1cd3a484-f3bd-45be-bf78-9013cc82eced)

## **Description**
**This Python project generates a QR code for a given URL and saves it as a PNG file.**
<br>Users provide a URL and a desired file name, and the application validates the URL, ensures the file name has the correct extension, creates the QR code, and saves it in a designated directory.


## **Features**
- **URL Validation** : Ensures the provided URL is valid before generating the QR code.
- **File Naming** : Automatically appends ".png" extension to the file name if not provided.
- **QR Code Generation** : Creates a QR code with customizable colors.
- **Logging** : Logs messages for successful QR code generation or any errors encountered.

## **Prerequisites**
- **Python 3.x** installed on your machine
- **qrcode** library
- **logging** library *(part of the Python Standard Library)*

## **Installation Instructions**
Make sure you have [Python](https://www.python.org/downloads/) installed on your system before running the scripts.

1. Clone this repository to your machine.
   
   ```bash
   git clone https://github.com/0x414854/QR_Code_Generator.git

2. Navigate to the repository directory.

   ```bash
    cd QR_Code_Generator

3. Install the required libraries.

   ```bash
   pip install qrcode

4. Run the 'qr_code_generator.py' script.
   
   ```bash
   python3 qr_code_generator.py

## **Usage Examples**
- Follow the prompts to enter a URL and file name.
- The script will validate the URL, generate the QR code, and save it as a PNG file in the 'QR_codes' directory.

## **Tree Directory**

QR_Code_Generator/
<br>├── QR_code_generator.py
<br>└── README.md

## **Future Updates**
- **Customizable QR Code Size** : Allow users to specify the size of the QR code.
- **Support for Different File Formats** : Enable saving QR codes in formats other than PNG, such as JPEG or SVG.
- **Logo in QR Code** : Add support for embedding a logo at the center of the QR code.

## **License**
This project is licensed under the **MIT License**.

## **Author**
[**0x414854**](https://github.com/0x414854)
