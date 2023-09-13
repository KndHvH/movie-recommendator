import os
import pandas as pd

class FileHelper():
    @staticmethod
    def get_dataframe(filename:str):
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_file_path = os.path.join(current_dir, 'database', filename)
        return pd.read_csv(data_file_path, delimiter=';')
