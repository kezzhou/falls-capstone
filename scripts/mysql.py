## Import Packages ##
import pandas as pd
import numpy as np
import datetime
import mysql.connector
import sqlalchemy
from mysql.connector import Error

## Determining dtypes for tables in Mysqlworkbench
df = pd.read_csv('./data/modified/diagnosis_mod.csv')
df.dtypes

df = pd.read_csv('./data/modified/encounter_mod.csv')
df.dtypes

df = pd.read_csv('./data/modified/lab_result_mod.csv')
df.dtypes

df = pd.read_csv('./data/modified/medication_drug_mod.csv')
df.dtypes

df = pd.read_csv('./data/modified/medication_ingredient_mod.csv')
df.dtypes

df = pd.read_csv('./data/modified/patient_mod.csv')
df.dtypes

df = pd.read_csv('./data/modified/standardized_terminology_mod.csv')
df.dtypes

df = pd.read_csv('./data/modified/vitals_signs_mod.csv')
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


## Drop existing tables

def drop_all_tables():
    try:
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            cursor = connection.cursor()

            # Get all table names in the database
            show_tables_query = "SHOW TABLES;"
            cursor.execute(show_tables_query)
            tables = [table[0] for table in cursor.fetchall()]

            # Drop each table
            for table in tables:
                drop_table_query = f"DROP TABLE IF EXISTS {table};"
                cursor.execute(drop_table_query)

            connection.commit()
            print("All tables dropped successfully.")

    except Error as e:
        print("Error while dropping tables:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    drop_all_tables()




# Define the table names and their corresponding schema

def create_connection():
    """Create a MySQL database connection."""
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MySQL database.")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def push_csv_to_table(connection, csv_file, table_name):
    """Push CSV data into an empty MySQL table."""
    try:
        df = pd.read_csv(csv_file)  # Read the CSV data into a pandas DataFrame
        if connection.is_connected():
            cursor = connection.cursor()

            # Create an empty table with the same columns as the DataFrame
            # Note: You may need to adjust data types and column names accordingly
            create_table_query = f"CREATE TABLE {table_name} ({', '.join([f'`{col}` TEXT' for col in df.columns])})"
            cursor.execute(create_table_query)

            # Insert the CSV data into the table
            for _, row in df.iterrows():
                insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['%s'] * len(df.columns))})"
                cursor.execute(insert_query, tuple(row))

            connection.commit()
            print("Data pushed successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    csv_file_path = "./data/modified/diagnosis_mod.csv"  # Replace with the actual path to your CSV file
    table_name = "diagnosis"  # Replace with the name of the empty table in MySQL


    connection = create_connection()
    if connection:
        push_csv_to_table(connection, csv_file_path, table_name)

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
