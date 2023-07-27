## Import Packages ##
import pandas as pd
import numpy as np
import datetime
import mysql.connector
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


# Replace these with your MySQL database credentials
host = 'localhost'
user = 'root'
password = ''
database = 'AHI_falls'

# Read the CSV file using pandas
diagnosis = pd.read_csv('data/modified/diagnosis_mod.csv')
encounter = pd.read_csv('data/modified/encounter_mod.csv')
lab_result = pd.read_csv('data/modified/lab_result_mod.csv')
medication_drug = pd.read_csv('data/modified/medication_drug_mod.csv')
medication_ingredient = pd.read_csv('data/modified/medication_ingredient_mod.csv')
patient = pd.read_csv('data/modified/patient_mod.csv')
standardized_terminology = pd.read_csv('data/modified/standardized_terminology_mod.csv')
vital_signs = pd.read_csv('data/modified/vital_signs_mod.csv')


# Connect to the MySQL database
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()

# Get the list of all tables in the database
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
print(tables)

# Drop each table one by one
for table in tables:
    table_name = table[0]
    drop_table_query = f"DROP TABLE IF EXISTS {table_name}"
    cursor.execute(drop_table_query)


# Define the table names and their corresponding schema
table1_name = 'diagnosis'
table1_schema = '''
    CREATE TABLE IF NOT EXISTS diagnosis (
        column1 INT,
        column2 VARCHAR(255),
        column3 FLOAT
    )
'''

table2_name = 'encounter'
table2_schema = '''
    CREATE TABLE IF NOT EXISTS encounter (
        column1 INT,
        column2 VARCHAR(255),
        column3 DATE
    )
'''

table3_name = 'lab_result'
table3_schema = '''
    CREATE TABLE IF NOT EXISTS lab_result (
        column1 INT,
        column2 VARCHAR(255),
        column3 DATE
    )
'''

table4_name = 'medication_drug'
table4_schema = '''
    CREATE TABLE IF NOT EXISTS medication_drug (
        column1 INT,
        column2 VARCHAR(255),
        column3 DATE
    )
'''

table5_name = 'medication_ingredient'
table5_schema = '''
    CREATE TABLE IF NOT EXISTS medication_ingredient (
        column1 INT,
        column2 VARCHAR(255),
        column3 DATE
    )
'''

table6_name = 'patient'
table6_schema = '''
    CREATE TABLE IF NOT EXISTS patient (
        column1 INT,
        column2 VARCHAR(255),
        column3 DATE
    )
'''

table7_name = 'standardized_terminology'
table7_schema = '''
    CREATE TABLE IF NOT EXISTS standardized_terminology (
        column1 INT,
        column2 VARCHAR(255),
        column3 DATE
    )
'''

table8_name = 'vital_signs'
table8_schema = '''
    CREATE TABLE IF NOT EXISTS vital_signs (
        column1 INT,
        column2 VARCHAR(255),
        column3 DATE
    )
'''
# Execute the SQL queries to create the tables
cursor.execute(table1_schema)
cursor.execute(table2_schema)
cursor.execute(table3_schema)
cursor.execute(table4_schema)
cursor.execute(table5_schema)
cursor.execute(table6_schema)
cursor.execute(table7_schema)
cursor.execute(table8_schema)

# Commit the changes to the database
conn.commit()

# Read data from CSV files using pandas
csv_file1 = 'data_table1.csv'  # Replace with the path to your CSV file for table1
csv_file2 = 'data_table2.csv'  # Replace with the path to your CSV file for table2

df_table1 = pd.read_csv(csv_file1)
df_table2 = pd.read_csv(csv_file2)

# Push data from CSV files to MySQL tables
df_table1.to_sql(table1_name, conn, if_exists='replace', index=False)
df_table2.to_sql(table2_name, conn, if_exists='replace', index=False)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

# Define the table name in your database where you want to insert the data
table_name = 'diagnosis'

# Create the table in the database (uncomment if needed)
# Note: Adjust the column names and data types according to your CSV file
# cursor.execute(f"CREATE TABLE {table_name} (col1 INT, col2 VARCHAR(255), col3 FLOAT)")

# Insert the data into the MySQL database
for index, row in diagnosis.iterrows():
    values = tuple(row)
    placeholders = ', '.join(['%s'] * len(row))
    query = f"INSERT INTO {table_name} VALUES ({placeholders})"
    cursor.execute(query, values)

# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()


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

