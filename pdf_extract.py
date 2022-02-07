try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pandas as pd 
from bs4 import BeautifulSoup
from pdf2image import convert_from_path
import os

data = pd.read_csv(r'Data Engineer Task - Data Engineer Task.csv', header=None)
urls = data[0]
for url in urls:
    if url.endswith('pdf'):
       print(url)
    else:
        print('page')