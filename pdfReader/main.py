import re 
from collections import Counter
from pyPDF2 import pdfReader

def extarct_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as pdf:
        reader = pdfReader(pdf_file, strict=False)
        print('Pages: ', len(reader.pages))
        print('-'*10)
        return [page.extract_text() for page in reader.pages]


def count_words(text_list):
    all_words = []
    for text in text_list:
        split_text = re.split(r'\s+|[,;?!.-]\s*', text.lower())
        all_words += [word for word in split_text if word]
        return Counter(all_words)
    

