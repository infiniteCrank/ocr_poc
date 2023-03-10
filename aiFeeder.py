from PIL import Image

import pytesseract

import tempfile

from pdf2image import convert_from_path

#convert pdf to jpg 
with tempfile.TemporaryDirectory() as path:
    images_from_path = convert_from_path("data/navy.pdf", fmt="jpeg", output_folder="data",output_file="testConvert", single_file=True,)

#take the image list and perform ocr on the generated images 
print(pytesseract.image_to_string(Image.open('data/testConvert.jpg')))