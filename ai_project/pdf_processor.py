
import pymupdf


def extract_text(pdf_file):

    doc = pymupdf.open(stream=pdf_file.read(), filetype="pdf")

    pages = []

    for page_number, page in enumerate(doc, start=1):

        text = page.get_text("text")

        if text.strip():
            pages.append({
                "page": page_number,
                "text": text
            })

    doc.close()

    return pages
