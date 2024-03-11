from docx import Document

'''pip install python-docx'''

def extract(filename):
    doc = Document(filename)
    fullText = []

    for para in doc.paragraphs:
        fullText.append(para.text)

    return ' '.join(fullText)
