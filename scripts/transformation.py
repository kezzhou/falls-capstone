## Import Packages ##
import pandas as pd
import numpy as np
import datetime
import mysql.connector
import sqlalchemy


## Data Cleaning and Transformation

## Combine tables and drop columns and duplicates ##

table1 = pd.read_csv('./data/original/diagnosis_falls.csv')
table2 = pd.read_csv('./data/original/diagnosis.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df.drop(columns=['encounter_id', 'principal_diagnosis_indicator', 'admitting_diagnosis', 'reason_for_visit','derived_by_TriNetX', 'source_id'], inplace=True)
df.dtypes
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df.dtypes
df.drop_duplicates()
df.to_csv('./data/modified/diagnosis_mod.csv')
df = pd.read_csv('./data/modified/diagnosis_mod.csv')
df.dtypes


table1 = pd.read_csv('./data/original/encounter_falls.csv')
table2 = pd.read_csv('./data/original/encounter.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df.drop(columns=['start_date_derived_by_TriNetX', 'end_date_derived_by_TriNetX', 'derived_by_TriNetX'], inplace=True)
df.dtypes
df['start_date'] = pd.to_datetime(df['start_date'], format='%Y%m%d')
df['end_date'] = pd.to_datetime(df['end_date'], format='%Y%m%d')
df.drop_duplicates()
df.to_csv('./data/modified/encounter_mod.csv')


table1 = pd.read_csv('./data/original/lab_result_falls.csv')
table2 = pd.read_csv('./data/original/lab_result.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df.drop(columns=['encounter_id', 'source_id', 'derived_by_TriNetX'], inplace=True)
df.dtypes
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df.drop_duplicates()
df.to_csv('./data/modified/lab_result_mod.csv')
df.dtypes

table1 = pd.read_csv('./data/original/medication_drug_falls.csv')
table2 = pd.read_csv('./data/original/medication_drug.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df.drop(columns=['encounter_id', 'unique_id', 'strength', 'quantity_dispensed','days_supply','derived_by_TriNetX', 'source_id'], inplace=True)
df.dtypes
df['start_date'] = pd.to_datetime(df['start_date'], format='%Y%m%d')
df.drop_duplicates()
df.to_csv('./data/modified/medication_drug_mod.csv')
df.dtypes

table1 = pd.read_csv('./data/original/medication_ingredient_falls.csv')
table2 = pd.read_csv('./data/original/medication_ingredient.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df.drop(columns=['encounter_id', 'unique_id', 'strength', 'brand','derived_by_TriNetX', 'source_id'], inplace=True)
df.dtypes
df['start_date'] = pd.to_datetime(df['start_date'], format='%Y%m%d')
df.drop_duplicates()
df.to_csv('./data/modified/medication_ingredient_mod.csv')
df.dtypes

table1 = pd.read_csv('./data/original/patient_falls.csv')
table2 = pd.read_csv('./data/original/patient.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df.drop(columns=['reason_yob_missing', 'patient_regional_location', 'source_id'], inplace=True)
df.dtypes
df['month_year_death'] = pd.to_datetime(df['month_year_death'], format='%Y%m')
df.drop_duplicates()
df.to_csv('./data/modified/patient_mod.csv')
df.dtypes

table1 = pd.read_csv('./data/original/standardized_terminology_falls.csv')
table2 = pd.read_csv('./data/original/standardized_terminology.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df.drop(columns=['path'], inplace=True)
df.dtypes
df.drop_duplicates()
df.to_csv('./data/modified/standardized_terminology_mod.csv')
df.dtypes

table1 = pd.read_csv('./data/original/vitals_signs_falls.csv')
table2 = pd.read_csv('./data/original/vitals_signs.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df.drop(columns=['derived_by_TriNetX', 'source_id'], inplace=True)
df.dtypes
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df.drop_duplicates()
df.to_csv('./data/modified/vitals_signs_mod.csv')
df.dtypes





