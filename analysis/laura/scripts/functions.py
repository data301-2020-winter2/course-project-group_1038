import pandas as pd
import numpy as np
import seaborn as sns

#analysis and cleaning

def load_process(path):
    data = pd.read_csv(path).drop(["id", "rated", "white_id", "black_id", "opening_ply"], axis=1)
    data = data[data['victory_status'] != 'outoftime']
    data.to_csv('../../data/processed/data.csv')
    return data

def hist_plot_openings()
    fig, ax = plt.subplots()
    fig.set_size_inches(5,200)
    openings = sns.histplot(df, y='opening_name', hue='winner', stat='count')
    return openings