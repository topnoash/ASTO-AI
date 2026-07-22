import fitz
import easyocr
import numpy as np
from PIL import Image

# Load OCR model once
reader = easyocr.Reader(['en'])

def extract_text(uploaded_file):

    # Read PDF into memory
    pdf_bytes = uploaded_file.read()

    # ---------- Try PyMuPDF first ----------
    pdf = fitz.open(stream=pdf_bytes, filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    # If enough text exists, return it
    if len(text.strip()) > 50:
        return text

    # ---------- OCR Fallback ----------
    pdf = fitz.open(stream=pdf_bytes, filetype="pdf")

    ocr_text = ""

    for page in pdf:

        pix = page.get_pixmap(dpi=300)

        img = Image.frombytes(
            "RGB",
            [pix.width, pix.height],
            pix.samples
        )

        img_np = np.array(img)

        result = reader.readtext(img_np, detail=0)

        ocr_text += "\n".join(result)

    pdf.close()

    return ocr_text