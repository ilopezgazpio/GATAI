import fitz  # PyMuPDF

'''pip install PyMuPDF'''

def extract(filename):
    doc = fitz.open(filename)
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()
    return text
