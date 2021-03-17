import pandas as pd


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

