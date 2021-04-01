import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pylab as plt 
import matplotlib.image as mpimg

from collections import defaultdict

#analysis and cleaning

def load_process(path):
    data = pd.read_csv(path).drop(["id", "rated", "white_id", "black_id", "opening_ply"], axis=1)
    data = data[data['victory_status'] != 'outoftime']
    data.to_csv('../../data/processed/data.csv')
    return data

def hist_plot_openings():
    fig, ax = plt.subplots()
    fig.set_size_inches(5,200)
    openings = sns.histplot(df, y='opening_name', hue='winner', stat='count')
    return openings

def load(path_to_dataframe: str):
    return pd.read_csv(path_to_dataframe)


def clean(df: pd.DataFrame, columns_to_drop: list[str]):
    return remove_out_of_time_games(df).drop(columns=columns_to_drop).dropna().reset_index(drop=True)


def remove_out_of_time_games(df: pd.DataFrame):
    return df[df["victory_status"] != "outoftime"]


def create_delta(df: pd.DataFrame, name: str, column1: str, column2: str):
    df[name] = df[column1] - df[column2]


def create_time_delta(df: pd.DataFrame):
    create_delta(df, "dt", "last_move_at", "created_at")


def clean_based_on_time_delta(df: pd.DataFrame):
    return df[df["dt"] > 0]


# this does it all really
def sort_by_time_taken(df: pd.DataFrame):
    create_time_delta(df)
    df = clean_based_on_time_delta(df)
    df.sort_values(by="dt", ascending=True)
    

def drop_uncommon_openings(df: pd.DataFrame, threshold: int=2):
    values = defaultdict(int)
    
    for opening in df["opening_eco"]:
        values[opening] += 1
    
    for opening, occurences in values.items():
        if occurences < threshold:
            df = df[df["opening_eco"] != opening]

    return df

    
    