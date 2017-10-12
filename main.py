#========================================================
# cordeirolibel and daviboberg - 2017
# https://github.com/cordeirolibel/Titanic/
#========================================================

import pandas as pd
import numpy as np

#   Dataframes
df_train = pd.read_csv('data/train.csv')
df_test = pd.read_csv('data/test.csv')

print(df_train.head())