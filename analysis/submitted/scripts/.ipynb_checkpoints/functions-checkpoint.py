import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pylab as plt 
import matplotlib.image as mpimg

from collections import defaultdict
from copy import deepcopy

#analysis and cleaning

class WinCount(defaultdict):
    def __init__(self) -> None:
        #self.dict = defaultdict(lambda: defaultdict(int))
        self.dict = defaultdict(lambda: {"white": 0, "black": 0, "draw": 0})
        
    def setup(self, df: pd.DataFrame, name_or_eco: str = "eco") -> None:
        """
        sets up the class instance's dict
        """
        if (name_or_eco := name_or_eco.lower()) not in ("eco", "name"):
                raise Exception(f"name_or_eco received invalid argument: {name_or_eco}")
                
        for _, row in df.iterrows():
            self.dict[row[f"opening_{name_or_eco}"]][row["winner"]] += 1
    
    @staticmethod
    def totals(_dict: defaultdict) -> defaultdict:
        """
        gathers white, black, and draw values and retunrns a {opening: total_wins} dict
        """
        d = defaultdict(int)
        for item, value in _dict.items():
            for _, _value in value.items():
                d[item] += _value
        return d
    
    def create_winner_specific_dict(self, winner: str) -> defaultdict:
        """
        returns winner specific dict
        """
        if (winner := winner.lower()) not in ("white", "black", "draw"):
                raise Exception(f"winner received invalid argument: {winner}")
                
        d = defaultdict(int)
        for item, value in self.dict.items():
            d[item] = value[winner]
            
        return d
    
    @staticmethod
    def sieve_winner_specific_dict(winner_dict: defaultdict, threshold: int):
        """
        takes in winner specific dict ei: white = {opening: wins} and returns the dict with wins above or equal to the threshold
        """
        d = deepcopy(winner_dict)
        for item, value in winner_dict.items():
            if value < threshold:
                del d[item]
        return d
    
    def sieve(self, threshold: int) -> defaultdict:
        """
        returns a copy of the WinCount instance's totals with win occurences above (or equal) to the threshold
        """
        d = deepcopy(self.dict)
        totals = self.totals(self.dict)
        for item, value in totals.items():
            if value < threshold:
                del d[item]
        return d

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

def remove_out_of_time_games(df: pd.DataFrame):
    return df[df["victory_status"] != "outoftime"]

def load(path_to_dataframe: str):
    return pd.read_csv(path_to_dataframe)


def clean(df: pd.DataFrame, columns_to_drop: list[str]):
    return remove_out_of_time_games(df).drop(columns=columns_to_drop).dropna().reset_index(drop=True)


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
