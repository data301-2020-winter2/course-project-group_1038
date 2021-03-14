import pandas as pd
import numpy as np
import seaborn as sns

def load_process(path):
    data = pd.read_csv(path)
        #analysis and cleaning
        data = data[data['victory_status'] != 'outoftime']
        data.drop([["id", "rated", "white_id", "black_id", "opening_ply"]])
        data.to_csv('../data/processed/data.csv')
    return data