import pandas as pd
import numpy as np
import seaborn as sns

#analysis and cleaning

def load_process(path):
    data = pd.read_csv(path).drop(["id", "rated", "white_id", "black_id", "opening_ply"], axis=1)
    data.to_csv('../../data/processed/data.csv')
    return data