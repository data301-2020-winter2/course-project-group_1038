{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "experienced-barbados",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt


def load_process(path):
    data = pd.read_csv(path).drop(["id", "rated", "white_id", "black_id", "opening_ply"], axis=1)
    data = data[data['victory_status'] != 'outoftime']
    data.to_csv('../../data/processed/data.csv')
    return data
