from chunker import create_chunks

pages=[
    {
        "page":1,
        "text":"python is a programming language"*40
    },
    {
        "page":2,
        "text":"python supports list and tuples"*30
    }
]

chunks=create_chunks(pages)

for i,chunk in enumerate(chunks,start=-1):
    print("Chunk:",i)
    print("Page:",chunk["page"])
    print("length:",len(chunk["text"]))
    print("text:",chunk["text"][:80])
    print("-----------------------")