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

##sex ####

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


## race ####
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

## ethnicity ###
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

## age ######
today = datetime.date.today()
year = today.year
print(year)

##falls patients
falls_df['age'] = year - falls_df['year_of_birth']
falls_df['age']

falls_df['age'].mean()
falls_df['age'].median()
falls_df['age'].max()
falls_df['age'].min()

##nonfalls patients
non_falls_df['age'] = year - non_falls_df['year_of_birth']
non_falls_df['age']

non_falls_df['age'].mean()
non_falls_df['age'].median()
non_falls_df['age'].max()
non_falls_df['age'].min()

## Histogram

# Function to map age into age ranges
def map_age_range(age):
    return f"{(age // 10) * 10}-{(age // 10) * 10 + 9}"

# Apply the mapping function to create a new column 'age_range' for both DataFrames
falls_df['age_range'] = falls_df['age'].map(map_age_range)
non_falls_df['age_range'] = non_falls_df['age'].map(map_age_range)

# Calculate the counts for each age range in falls and non-falls patients
falls_age_counts = falls_df['age_range'].value_counts().sort_index()
non_falls_age_counts = non_falls_df['age_range'].value_counts().sort_index()

# Create histogram charts for falls and non-falls patients
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(falls_age_counts.index, falls_age_counts.values)
plt.title("Age distribution for falls patients")
plt.xlabel("Age Range")
plt.ylabel("Counts")

plt.subplot(1, 2, 2)
plt.bar(non_falls_age_counts.index, non_falls_age_counts.values)
plt.title("Age distribution for non-falls patients")
plt.xlabel("Age Range")
plt.ylabel("Counts")

plt.tight_layout()
plt.show()


### Diagnoses ###

df = pd.read_csv('./data/original/diagnosis_falls.csv')
df.drop_duplicates
df1 = pd.read_csv('./data/original/standardized_terminology_falls.csv')
df1.drop_duplicates
merged_df = pd.merge(df, df1, on='code', how='left')

merged_df['date'] = pd.to_datetime(merged_df['date'], format='%Y%m%d')



### counting diagnoses per patient
# Group by 'patient_id' and count the occurrences of each 'code'
code_counts = merged_df.groupby('patient_id')['code'].count()

# Perform descriptive statistics on the code counts
code_counts_stats = code_counts.describe()

# Print descriptive statistics
print("Descriptive Statistics for 'code' counts per 'patient_id':")
print(code_counts_stats)

# Create a bar chart to visualize the code counts
plt.bar(code_counts.index, code_counts.values, color='skyblue')
plt.xlabel('Patient ID')
plt.ylabel('Number of Codes')
plt.title('Number of Codes per Falls Patient')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



## falls over time
falls_by_date = merged_df['date'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(falls_by_date.index, falls_by_date.values, marker='o')
plt.xlabel('Date')
plt.ylabel('Number of Falls Diagnoses')
plt.title('Falls Diagnoses Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Count the occurrences of each unique code_description
code_description_counts = merged_df['code_description'].value_counts()
print(code_description_counts)

# Find the most common code description
most_common_code_description = code_description_counts.idxmax()
most_common_count = code_description_counts.max()

# Plot the bar graph
plt.figure(figsize=(10, 6))
code_description_counts.plot(kind='bar')
plt.xlabel('Code Description')
plt.ylabel('Count')
plt.title('Count of Code Description for Falls Diagnoses')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Add text annotation for the most common code description
plt.annotate(f"Most Common: {most_common_code_description} ({most_common_count} times)",
             xy=(0, most_common_count), xytext=(0.5, most_common_count + 10),
             arrowprops=dict(facecolor='black', arrowstyle="->"))

plt.show()

## non falls ##
df = pd.read_csv('./data/original/diagnosis.csv')
df.drop_duplicates
df1 = pd.read_csv('./data/original/standardized_terminology.csv')
df1.drop_duplicates
merged_df = pd.merge(df, df1, on='code', how='left')

merged_df['date'] = pd.to_datetime(merged_df['date'], format='%Y%m%d')


### counting diagnoses per nonfall patient
# Group by 'patient_id' and count the occurrences of each 'code'
code_counts = merged_df.groupby('patient_id')['code'].count()

# Perform descriptive statistics on the code counts
code_counts_stats = code_counts.describe()

# Print descriptive statistics
print("Descriptive Statistics for 'code' counts per 'patient_id':")
print(code_counts_stats)

# Create a bar chart to visualize the code counts
plt.bar(code_counts.index, code_counts.values, color='skyblue')
plt.xlabel('Patient ID')
plt.ylabel('Number of Codes')
plt.title('Number of Codes per Nonfalls Patient')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

## Diagnoses over time for nonfalls 
nonfalls_by_date = merged_df['date'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(falls_by_date.index, falls_by_date.values, marker='o')
plt.xlabel('Date')
plt.ylabel('Number of Nonfalls Diagnoses')
plt.title('Nonfalls Diagnoses Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Count the occurrences of each unique code_description
code_description_counts = merged_df['code_description'].value_counts()
print(code_description_counts)

# Find the most common code description
most_common_code_description = code_description_counts.idxmax()
most_common_count = code_description_counts.max()

# Plot the bar graph
plt.figure(figsize=(10, 6))
code_description_counts.plot(kind='bar')
plt.xlabel('Code Description')
plt.ylabel('Count')
plt.title('Count of Code Description for Nonfalls Diagnoses')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Add text annotation for the most common code description
plt.annotate(f"Most Common: {most_common_code_description} ({most_common_count} times)",
             xy=(0, most_common_count), xytext=(0.5, most_common_count + 10),
             arrowprops=dict(facecolor='black', arrowstyle="->"))

plt.show()




## encounters ######

df = pd.read_csv('./data/original/encounter_falls.csv')
df.drop_duplicates
df['start_date'] = pd.to_datetime(df['start_date'], format='%Y%m%d')
df['end_date'] = pd.to_datetime(df['end_date'], format='%Y%m%d')


type_counts = df['type'].value_counts()

# Plot the bar chart
plt.figure(figsize=(8, 6))
type_counts.plot(kind='bar')
plt.xlabel('Encounter Type')
plt.ylabel('Count')
plt.title('Count of Encounter Types for Falls Patients')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()

# Calculate the difference between 'end_date' and 'start_date'
df['length'] = df['end_date'] - df['start_date']

# Convert the timedelta to numeric (in days)
df['length'] = df['length'].dt.days

# Run descriptive statistics on the 'length' column
descriptive_stats = df['length'].describe()

print(descriptive_stats)


## non falls

df = pd.read_csv('./data/original/encounter.csv')
df.drop_duplicates
df['start_date'] = pd.to_datetime(df['start_date'], format='%Y%m%d')
df['end_date'] = pd.to_datetime(df['end_date'], format='%Y%m%d')


type_counts = df['type'].value_counts()

# Plot the bar chart
plt.figure(figsize=(8, 6))
type_counts.plot(kind='bar')
plt.xlabel('Encounter Type')
plt.ylabel('Count')
plt.title('Count of Encounter Types for Nonfalls Patients')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()

# Calculate the difference between 'end_date' and 'start_date'
df['length'] = df['end_date'] - df['start_date']

# Convert the timedelta to numeric (in days)
df['length'] = df['length'].dt.days

# Run descriptive statistics on the 'length' column
descriptive_stats = df['length'].describe()

print(descriptive_stats)



### lab results ####
# Read the CSV file into a DataFrame
df_lab_result_falls = pd.read_csv('./data/original/lab_result_falls.csv')

# Group by 'patient_id' and count the occurrences of each 'code'
code_counts_per_patient = df_lab_result_falls.groupby('patient_id')['code'].count()

# Print the result
print("Number of 'code' per unique 'patient_id':")
print(code_counts_per_patient)

