import os
import qrcode
import re
import logging

"""
This script generates a QR code for a given URL and saves it as a PNG file.
The user provides the URL and the desired file name, and the script validates the URL,
ensures the file name has the correct extension, creates the QR code, and saves it in a designated directory.
"""

def get_input(prompt):
    return input(prompt).strip()

def validate_file_name(file_name):
    if not file_name.endswith(".png"):
        file_name += ".png"
    return file_name

def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  
        r'localhost|'  
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  
        r'(?::\d+)?'  
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def generate_qr_code(data, file_path, file_name, fill_color="black", back_color="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(os.path.join(file_path, file_name))

def main():
    logging.basicConfig(level=logging.INFO)
    
    data = get_input("Enter URL link : ")
    if not is_valid_url(data):
        logging.error("The URL provided is not valid. Please enter a valid URL.")
        return
    
    file_name = validate_file_name(get_input("Enter the file name : "))
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'QR_codes')
    
    os.makedirs(file_path, exist_ok=True)

    try:
        generate_qr_code(data, file_path, file_name)
        logging.info(f"QR code successfully generated in the file {file_name} in the path {file_path}")
    except Exception as e:
        logging.error(f"An error occurred while generating the QR code : {e}")

if __name__ == "__main__":
    main()
