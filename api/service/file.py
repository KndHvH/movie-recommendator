import os
import pandas as pd

class FileService():
    @staticmethod
    def get_dataframe():
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_file_path = os.path.join(current_dir, 'data', 'all_movies.csv')
        return pd.read_csv(data_file_path, delimiter=';')
