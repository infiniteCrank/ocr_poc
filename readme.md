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

## Set Up NLP 
### Steps: 
1. download Apache Open NLP (Here)[https://opennlp.apache.org/download.html]
2. OpenNLP script uses ```JAVA_CMD``` and ```JAVA_HOME``` variables to determine which command to use to execute Java virtual machine.
3. OpenNLP script uses ```OPENNLP_HOME``` variable to determine the location of the binary distribution of OpenNLP. It is recommended to point this variable to the binary distribution of current OpenNLP version and update PATH variable to include ```$OPENNLP_HOME/bin```
4. if this is done correctly you should now be able to run ```opennlp```
5. next you will need to download the english sentence model from (Here)[https://www.apache.org/dyn/closer.cgi/opennlp/models/ud-models-1.0/opennlp-en-ud-ewt-sentence-1.0-1.9.3.bin]. I have downloaded it and renamed it ```en-sent.bin``` and placed it in the models folder. 
6. next you will need to download the english Token model from (Here)[https://www.apache.org/dyn/closer.cgi/opennlp/models/ud-models-1.0/opennlp-de-ud-gsd-tokens-1.0-1.9.3.bin]. I have downloaded it and renamed it ```en-token.bin``` and placed it in the models folder. 
7. download pre-trained name finder models (Here)[https://opennlp.sourceforge.net/models-1.5/]
8. I have downloaded some that I think might be useful for this form and placed them in models directory
9. eventually it would be best to train my own model for a specific standard form I am processing

## What is NLP Natural Language Processor?
1. NLP takes text and parses it to extract important information 
2. It breaks text into sentences by putting each sentence on its own line 
3. It then takes each sentence and breaks it apart into words and punctuation called tokens
4. the last part it does is based off training it can tag tokens it finds and give them a specific label like Name or address 

### Running project:
1. ```python3 aiFeeder.py```
2. ```opennlp SentenceDetector models/en-sent.bin < text_from_JPG.txt > text_to_sentences.txt```
3. ```opennlp TokenizerME models/en-token.bin < text_to_sentences.txt > sentences-tokenized.txt```
4. ```opennlp TokenNameFinder models/en-ner-person.bin < sentences-tokenized.txt > found-person.txt```
5. ```opennlp TokenNameFinder models/es-ner-person-conll02.bin < sentences-tokenized.txt > found-person-conll02.txt``` this model did not work as well as the previous model
### What is this is doing:

### Important Links:
(tesseract Docs)[https://github.com/tesseract-ocr/tesseract]
(python tesseract Docs)[https://github.com/madmaze/pytesseract]
(python tesseract usage)[https://pypi.org/project/pytesseract/]
(pdf to image python library)[https://pdf2image.readthedocs.io/en/latest/overview.html]
(Apache NLP manual)[https://opennlp.apache.org/docs/2.1.1/manual/opennlp.html]

