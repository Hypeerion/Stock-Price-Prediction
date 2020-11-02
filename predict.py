# importing relevant modules
import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

# reading in data to df
df = pd.read_csv('sphist.csv')

# converting date col to datetime
df['Date'] = pd.to_datetime(df.Date)

# sorting data by date
df = df.sort_values('Date')

# creating five day average column
df['five_day'] = np.nan

#calculated rolling previous 5day price avg
for index, row in df.iterrows():
    row['five_day'] = 10
    

print(df.head(10))

