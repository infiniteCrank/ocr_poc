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

## Set Up NLP 
### Steps: 
1. download Apache Open NLP (Here)[https://opennlp.apache.org/download.html]
2. OpenNLP script uses ```JAVA_CMD``` and ```JAVA_HOME``` variables to determine which command to use to execute Java virtual machine.
3. OpenNLP script uses ```OPENNLP_HOME``` variable to determine the location of the binary distribution of OpenNLP. It is recommended to point this variable to the binary distribution of current OpenNLP version and update PATH variable to include ```$OPENNLP_HOME/bin```

### Important Links:
(Apache NLP manual)[https://opennlp.apache.org/docs/2.1.1/manual/opennlp.html]
