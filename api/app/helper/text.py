import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords

class TextHelper():
    @staticmethod
    def get_clean_text(text):
        text = text.lower()
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        text = tokenizer.tokenize(text)
        text = [word for word in text if word not in stopwords.words('portuguese')]
        return ' '.join(text)
    
    @staticmethod
    def get_vectorized_matrix(df:pd.DataFrame, column:str):
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(df[column])
        return tfidf_matrix
        