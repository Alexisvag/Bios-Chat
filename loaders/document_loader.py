from PyPDF2 import PdfReader
import docx
import pandas as pd


def extract_text(file):

    extension = file.name.split(".")[-1].lower()

    text = ""

    if extension == "pdf":

        pdf = PdfReader(file)

        for page in pdf.pages:
            text += page.extract_text() or ""

    elif extension == "docx":

        doc = docx.Document(file)

        for p in doc.paragraphs:
            text += p.text + "\n"

    elif extension == "txt":

        text = file.getvalue().decode("utf-8")

    elif extension == "xlsx":

        df = pd.read_excel(file)
        text = df.to_string(index=False)

    return text