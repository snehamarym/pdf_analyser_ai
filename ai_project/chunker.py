def create_chunks(pages,chunk_size=500,overlap=100):
    chunks=[]


    for page in pages:
        text=page["text"]
        page_number=page["page"]

        start=0

        while start< len(text):
            end=start+ chunk_size

            chunk_text=text[start:end]

            if chunk_text.strip():
                chunks.append({
                    "page":page_number,
                    "text":chunk_text
                })
            start+=chunk_size -overlap

        return chunks