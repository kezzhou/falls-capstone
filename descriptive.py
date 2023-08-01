## Import Packages ##
import pandas as pd
import numpy as np
import datetime
import mysql.connector
import sqlalchemy


## Data Cleaning and Transformation

## Combine tables and drop columns and duplicates ##

table1 = pd.read_csv('data/original/diagnosis_falls.csv')
table2 = pd.read_csv('data/original/diagnosis.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df.drop(columns=['encounter_id', 'principal_diagnosis_indicator', 'admitting_diagnosis', 'reason_for_visit','derived_by_TriNetX', 'source_id'], inplace=True)
df.dtypes
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df.drop_duplicates()
df.to_csv('data/modified/diagnosis_mod.csv')


table1 = pd.read_csv('data/original/encounter_falls.csv')
table2 = pd.read_csv('data/original/encounter.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df.drop(columns=['start_date_derived_by_TriNetX', 'end_date_derived_by_TriNetX', 'derived_by_TriNetX'], inplace=True)
df.dtypes
df['start_date'] = pd.to_datetime(df['start_date'], format='%Y%m%d')
df['end_date'] = pd.to_datetime(df['end_date'], format='%Y%m%d')
df.drop_duplicates()
df.to_csv('data/modified/encounter_mod.csv')


table1 = pd.read_csv('data/original/lab_result_falls.csv')
table2 = pd.read_csv('data/original/lab_result.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df.drop(columns=['encounter_id', 'source_id', 'derived_by_TriNetX'], inplace=True)
df.dtypes
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df.drop_duplicates()
df.to_csv('data/modified/lab_result_mod.csv')
df.dtypes

table1 = pd.read_csv('data/original/medication_drug_falls.csv')
table2 = pd.read_csv('data/original/medication_drug.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df.drop(columns=['encounter_id', 'unique_id', 'strength', 'quantity_dispensed','days_supply','derived_by_TriNetX', 'source_id'], inplace=True)
df.dtypes
df['start_date'] = pd.to_datetime(df['start_date'], format='%Y%m%d')
df.drop_duplicates()
df.to_csv('data/modified/medication_drug_mod.csv')
df.dtypes

table1 = pd.read_csv('data/original/medication_ingredient_falls.csv')
table2 = pd.read_csv('data/original/medication_ingredient.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df.drop(columns=['encounter_id', 'unique_id', 'strength', 'brand','derived_by_TriNetX', 'source_id'], inplace=True)
df.dtypes
df['start_date'] = pd.to_datetime(df['start_date'], format='%Y%m%d')
df.drop_duplicates()
df.to_csv('data/modified/medication_ingredient_mod.csv')
df.dtypes

table1 = pd.read_csv('data/original/patient_falls.csv')
table2 = pd.read_csv('data/original/patient.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df = pd.read_csv("data/original/patient.csv")
df.drop(columns=['reason_yob_missing', 'patient_regional_location', 'source_id'], inplace=True)
df.dtypes
df['month_year_death'] = pd.to_datetime(df['month_year_death'], format='%Y%m')
df.drop_duplicates()
df.to_csv('data/modified/patient_mod.csv')
df.dtypes

table1 = pd.read_csv('data/original/standardized_terminology_falls.csv')
table2 = pd.read_csv('data/original/standardized_terminology.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df = pd.read_csv("data/original/standardized_terminology.csv")
df.drop(columns=['path'], inplace=True)
df.dtypes
df.drop_duplicates()
df.to_csv('data/modified/standardized_terminology_mod.csv')
df.dtypes

table1 = pd.read_csv('data/original/vitals_signs_falls.csv')
table2 = pd.read_csv('data/original/vitals_signs.csv')
# Concatenate the two DataFrames vertically (row-wise)
df = pd.concat([table1, table2], ignore_index=True)
df = pd.read_csv("data/original/vitals_signs.csv")
df.drop(columns=['derived_by_TriNetX', 'source_id'], inplace=True)
df.dtypes
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df.drop_duplicates()
df.to_csv('data/modified/vitals_signs_mod.csv')
df.dtypes



## Pushing Data into MySqlWorkbench

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'AHI_Falls',
}

# Connect to the MySQL database
conn = mysql.connector.connect(**db_config)
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

table8_name = 'vitals_signs'
table8_schema = '''
    CREATE TABLE IF NOT EXISTS vitals_signs (
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
csv_file1 = 'data/modified/diagnosis_mod.csv' 
csv_file2 = 'data/modified/encounter_mod.csv'
csv_file3 = 'data/modified/lab_result_mod.csv'
csv_file4 = 'data/modified/medication_drug_mod.csv'
csv_file5 = 'data/modified/medication_ingredient_mod.csv'  
csv_file6 = 'data/modified/patient_mod.csv'
csv_file7 = 'data/modified/standardized_terminology_mod.csv'
csv_file8 = 'data/modified/vitals_signs_mod.csv'

# Read the CSV file using pandas
diagnosis = pd.read_csv('data/modified/diagnosis_mod.csv')
encounter = pd.read_csv('data/modified/encounter_mod.csv')
lab_result = pd.read_csv('data/modified/lab_result_mod.csv')
medication_drug = pd.read_csv('data/modified/medication_drug_mod.csv')
medication_ingredient = pd.read_csv('data/modified/medication_ingredient_mod.csv')
patient = pd.read_csv('data/modified/patient_mod.csv')
standardized_terminology = pd.read_csv('data/modified/standardized_terminology_mod.csv')
vitals_signs = pd.read_csv('data/modified/vitals_signs_mod.csv')

df_table1 = pd.read_csv(csv_file1)
df_table2 = pd.read_csv(csv_file2)
df_table3 = pd.read_csv(csv_file3)
df_table4 = pd.read_csv(csv_file4)
df_table5 = pd.read_csv(csv_file5)
df_table6 = pd.read_csv(csv_file6)
df_table7 = pd.read_csv(csv_file7)
df_table8 = pd.read_csv(csv_file8)

# Push data from CSV files to MySQL tables
df_table1.to_sql(table1_name, conn, if_exists='replace', index=False)
df_table2.to_sql(table2_name, conn, if_exists='replace', index=False)
df_table3.to_sql(table3_name, conn, if_exists='replace', index=False)
df_table4.to_sql(table4_name, conn, if_exists='replace', index=False)
df_table5.to_sql(table5_name, conn, if_exists='replace', index=False)
df_table6.to_sql(table6_name, conn, if_exists='replace', index=False)
df_table7.to_sql(table7_name, conn, if_exists='replace', index=False)
df_table8.to_sql(table8_name, conn, if_exists='replace', index=False)

# Commit the changes to the database
conn.commit()

# Let's make some new tables with joins for ease of use

# SQL query for left join and creating a new table
query = '''
CREATE TABLE diagnosis_patient AS
SELECT *
FROM diagnosis
LEFT JOIN patient
ON diagnosis.patient_id = patient.patient_id;
'''

# Execute the SQL query
cursor.execute(query)
conn.commit()


# Optional: Read the new table into a pandas DataFrame to verify the results
conn = mysql.connector.connect(**db_config)
query = 'SELECT * FROM diagnosis_patient;'
df_diagnosis_patient = pd.read_sql(query, conn)
conn.close()

# Print the DataFrame to see the new table data
print(df_diagnosis_patient)



# Close the cursor and connection
cursor.close()
conn.close()


## Demographic Data Analysis ##

# Connect to the MySQL database
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()

table_name = 'patient'

# Query to fetch all data from the table
query = f"SELECT * FROM {table_name}"

# Use pandas read_sql function to fetch data from the database and store it as a DataFrame
df = pd.read_sql(query, conn)

# Close the connection
cursor.close()
conn.close()



## Basic descriptive stats

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

