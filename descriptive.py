## Import Packages ##
import pandas as pd
import numpy as np
import datetime
import mysql.connector as msql
import sqlalchemy


## Data Cleaning and Transformation

df = pd.read_csv("data/original/diagnosis.csv")
df.drop(columns=['encounter_id', 'principal_diagnosis_indicator', 'admitting_diagnosis', 'reason_for_visit','derived_by_TriNetX', 'source_id'], inplace=True)
df.dtypes
df.drop_duplicates()
df.to_csv('data/modified/diagnosis_mod.csv')


df = pd.read_csv("data/original/encounter.csv")
df.drop(columns=['start_date_derived_by_TriNetX', 'end_date_derived_by_TriNetX', 'derived_by_TriNetX'], inplace=True)
df.dtypes
df.drop_duplicates()
df.to_csv('data/modified/encounter_mod.csv')
df.dtypes

df = pd.read_csv("data/original/lab_result.csv")
df.drop(columns=['encounter_id', 'source_id', 'derived_by_TriNetX'], inplace=True)
df.dtypes
df.drop_duplicates()
df.to_csv('data/modified/lab_result_mod.csv')
df.dtypes

df = pd.read_csv("data/original/medication_drug.csv")
df.drop(columns=['encounter_id', 'unique_id', 'strength', 'quantity_dispensed','days_supply','derived_by_TriNetX', 'source_id'], inplace=True)
df.dtypes
df.drop_duplicates()
df.to_csv('data/modified/medication_drug_mod.csv')
df.dtypes

df = pd.read_csv("data/original/medication_ingredient.csv")
df.drop(columns=['encounter_id', 'unique_id', 'strength', 'brand','derived_by_TriNetX', 'source_id'], inplace=True)
df.dtypes
df.drop_duplicates()
df.to_csv('data/modified/medication_ingredient_mod.csv')
df.dtypes

df = pd.read_csv("data/original/patient.csv")
df.drop(columns=['reason_yob_missing', 'patient_regional_location', 'source_id'], inplace=True)
df.dtypes
df.drop_duplicates()
df.to_csv('data/modified/patient_mod.csv')
df.dtypes

df = pd.read_csv("data/original/standardized_terminology.csv")
df.drop(columns=['path'], inplace=True)
df.dtypes
df.drop_duplicates()
df.to_csv('data/modified/standardized_terminology_mod.csv')
df.dtypes

df = pd.read_csv("data/original/vital_signs.csv")
df.drop(columns=['derived_by_TriNetX', 'source_id'], inplace=True)
df.dtypes
df.drop_duplicates()
df.to_csv('data/modified/vital_signs_mod.csv')
df.dtypes



## Pushing Data into MySqlWorkbench


from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', user='root',  
                        password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE AHI_falls")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)

# import the module
from sqlalchemy import create_engine
# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"  
                      .format(user="root", pw="", 
                      db="AHI_falls"))
# Insert whole DataFrame into MySQL
irisData.to_sql('iris', con = engine, if_exists = 'append', chunksize = 1000,index=False)


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

