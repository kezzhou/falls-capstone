## Import Packages ##
import pandas as pd
import numpy as np
import datetime

## Demographic Data ##

df = pd.read_csv("data/patient.csv")

df.head()

df.describe()


## sex
df.groupby('sex').count() / len(df)
# patient data has roughly even gender distribution, at 54.3 percent Female and 45.7 percent Male

## race
df.groupby('race').count() / len(df)
# mostly white

## ethnicity
# some unknown races seem to correlate to hispanic
df.groupby('ethnicity').count() / len(df)

## age
today = datetime.date.today()
year = today.year
print(year)

df['age'] = year - df['year_of_birth']
df['age']
df

df['age'].mean()
df['age'].median()
df['age'].max()
df['age'].min()

