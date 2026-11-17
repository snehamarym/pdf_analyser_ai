import pymupdf
from pdf_processor import extract_text

doc=pymupdf.open()
page=doc.new_page()
page.insert_text(
    
(50,50),"python is a programming language"
                 )
page=doc.new_page()
page.insert_text(
    (50,50),"python supports lists,tuples,and dictionaries."
)

doc.save("sample.pdf")
doc.close()
with open("sample.pdf","rb") as pdf:
    result=extract_text(pdf)

for item in result:
    print("page:",item["page"])
    print("text:",item["text"])
    print("----------------")