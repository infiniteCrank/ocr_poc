# Julian's OCR POC
## Description: This is a Proof of Concept that of an OCR that scans images to structured text.
### Install Steps:
1. Install Python 3.11
2. add ``` /Library/Frameworks/Python.framework/Versions/3.11/bin ``` to PATH
3. Install Pillow ``` python3 -m pip install --upgrade pip ``` ``` python3 -m pip install --upgrade Pillow```
4. Install pdf to image for python ``` python3 -m pip install --upgrade pdf2image ```
5. Install python-tesseract ``` python3 -m pip install --upgrade pytesseract ```
6. Install Home Brew ``` /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" ```
7. ``` brew install tesseract ```
8. ``` brew install poppler ```
### Test Tesseract:
1. to test install run ``` brew info tesseract ``` you can also get the install directory at this point if you need it.mine was /usr/local/Cellar/tesseract/5.3.0_1
2. test tesseract works by opening up terminal and navigating to data folder of this project. then run ``` tesseract test.jpg myTest ``` this should generate a text file called myTest.txt with text extracted from test.jpg
### Running project:
if this works you can now open terminal and navigate to this projects root and run ``` python3 ocr.py ```
### What is this is doing:
1. the first thing this does is convert images to strings in various ways to test Tesseract's capabilities.
2. The next thing this does is convert a pdf form to a JPG image then convert that image to Text 
### Important Links:
(tesseract Docs)[https://github.com/tesseract-ocr/tesseract]
(python tesseract Docs)[https://github.com/madmaze/pytesseract]
(python tesseract usage)[https://pypi.org/project/pytesseract/]
(pdf to image python library)[https://pdf2image.readthedocs.io/en/latest/overview.html]
