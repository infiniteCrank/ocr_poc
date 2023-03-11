from PIL import Image

import pytesseract

import tempfile

from pdf2image import convert_from_path

import subprocess


#convert pdf to jpg 
with tempfile.TemporaryDirectory() as path:
    images_from_path = convert_from_path("data/navy.pdf", fmt="jpeg", output_folder="data",output_file="testConvert", single_file=True,)

#take the generated image  and perform ocr 
textFromJPG = pytesseract.image_to_string(Image.open('data/testConvert.jpg'))
#wite text from the OCR to a text file 
text_file = open("text_from_JPG.txt", "w")
n = text_file.write(textFromJPG)
text_file.close()

# list_files = subprocess.run(["ls", "-l"])
# print("The exit code was: %d" % list_files.returncode)

# useless_cat_call = subprocess.run(["cat"], 
#                                   stdout=subprocess.PIPE, 
#                                   text=True, 
#                                   input="Hello from the other side")
# print(useless_cat_call.stdout)  