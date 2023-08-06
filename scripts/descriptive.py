## Import Packages ##
import pandas as pd
import numpy as np
import datetime
import mysql.connector
import sqlalchemy
import matplotlib.pyplot as plt

## Demographic Data Analysis ##

## Basic descriptive stats
falls_df = pd.read_csv('./data/original/patient_falls.csv')
non_falls_df = pd.read_csv('./data/original/patient.csv')
falls_df.drop_duplicates()
non_falls_df.drop_duplicates()

##sex

# Calculate the male/female ratio for falls patients
falls_ratio = falls_df['sex'].value_counts(normalize=True)

# Calculate the male/female ratio for non-falls patients
non_falls_ratio = non_falls_df['sex'].value_counts(normalize=True)

# Compare the ratios
print("Male/Female ratio for falls patients:")
print(falls_ratio)

print("\nMale/Female ratio for non-falls patients:")
print(non_falls_ratio)

# Visualize the ratios as bar charts
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Bar chart for falls patients
axes[0].bar(falls_ratio.index, falls_ratio.values)
axes[0].set_title("Male/Female ratio for falls patients")
axes[0].set_ylabel("Ratio")
axes[0].set_xlabel("Sex")

# Bar chart for non-falls patients
axes[1].bar(non_falls_ratio.index, non_falls_ratio.values)
axes[1].set_title("Male/Female ratio for non-falls patients")
axes[1].set_ylabel("Ratio")
axes[1].set_xlabel("Sex")

plt.tight_layout()
plt.show()


## race
# Counts for race in falls patients
falls_ratio = falls_df['race'].value_counts(normalize=True)

# Counts for race in non-falls patients
non_falls_ratio = non_falls_df['race'].value_counts(normalize=True)

# Visualize the counts as bar charts
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Bar chart for falls patients
axes[0].bar(falls_ratio.index, falls_ratio.values)
axes[0].set_title("Race distribution for falls patients")
axes[0].set_ylabel("Counts")
axes[0].set_xlabel("Race")

# Bar chart for non-falls patients
axes[1].bar(non_falls_ratio.index, non_falls_ratio.values)
axes[1].set_title("Race distribution for non-falls patients")
axes[1].set_ylabel("Counts")
axes[1].set_xlabel("Race")

plt.tight_layout()
plt.show()

## ethnicity
# Counts for race in falls patients
falls_ratio = falls_df['ethnicity'].value_counts(normalize=True)

# Counts for race in non-falls patients
non_falls_ratio = non_falls_df['ethnicity'].value_counts(normalize=True)

# Visualize the counts as bar charts
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Bar chart for falls patients
axes[0].bar(falls_ratio.index, falls_ratio.values)
axes[0].set_title("Ethnicity distribution for falls patients")
axes[0].set_ylabel("Counts")
axes[0].set_xlabel("Ethnicity")

# Bar chart for non-falls patients
axes[1].bar(non_falls_ratio.index, non_falls_ratio.values)
axes[1].set_title("Ethnicity distribution for non-falls patients")
axes[1].set_ylabel("Counts")
axes[1].set_xlabel("Ethnicity")

plt.tight_layout()
plt.show()

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

