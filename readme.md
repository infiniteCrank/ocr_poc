# Install Python 3.11
# add ``` /Library/Frameworks/Python.framework/Versions/3.11/bin ``` to PATH
# Install Pillow ``` python3 -m pip install --upgrade pip ``` ``` python3 -m pip install --upgrade Pillow```
# Install pdf to image for python ``` python3 -m pip install --upgrade pdf2image ```
# Install Home Brew ``` /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" ```
# ``` brew install tesseract ```
# ``` brew install poppler ```
# The tesseract directory can then be found using ``` brew info tesseract````
# mine was /usr/local/Cellar/tesseract/5.3.0_1
# test tesseract by opening up terminal and navigating to data folder then run ``` tesseract test.jpg myTest ``` this should generate a text file called myTest.txt with text extracted from test.jpg
# if this works you can now open terminal and navigate to this projects root and run ``` python3 ocr.py ```
# this will print text from each of these test images 
# Install python-tesseract ``` python3 -m pip install --upgrade pytesseract ```
# (tesseract Docs)[https://github.com/tesseract-ocr/tesseract]
# (python tesseract Docs)[https://github.com/madmaze/pytesseract]
# (python tesseract usage)[https://pypi.org/project/pytesseract/]
# (pdf to image python library)[https://pdf2image.readthedocs.io/en/latest/overview.html]
