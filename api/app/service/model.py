import pandas as pd
from sklearn.neighbors import NearestNeighbors

class ModelService():

    @staticmethod
    def get_model_with_tfidf(tfidf_matrix:pd.DataFrame):
        return NearestNeighbors(n_neighbors=100, metric='cosine').fit(tfidf_matrix)