from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def retrieve_chunks(chunks,question,top_k=3):
    documents=[chunks["text"]for chunk in chunks]
    vectorizer=TfidfVectorizer()

    document_vectors=vectorizer.fit_transform(documents)

    question_vector=vectorizer.transform([question])