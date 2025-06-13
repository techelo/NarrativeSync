import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def normalize_articles(articles):
    df = pd.DataFrame(articles)
    df = df.dropna(subset=["title"])
    return df

def compute_similarity(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['title'])
    similarity = cosine_similarity(tfidf_matrix)
    return similarity
