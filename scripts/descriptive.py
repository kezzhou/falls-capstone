## Import Packages ##
import pandas as pd
import numpy as np
import datetime
import mysql.connector
import sqlalchemy

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

import mysql.connector
import pandas as pd

# Replace the following variables with your MySQL database connection details
host = 'your_host'
user = 'your_username'
password = 'your_password'
database = 'your_database_name'
table_name = 'your_table_name'

# Connect to the MySQL server
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if connection.is_connected():
        print('Connected to MySQL database')

        # Query to fetch the data from the table
        query = f"SELECT * FROM {table_name};"

        # Read the data into a Pandas DataFrame
        df = pd.read_sql_query(query, connection)

        # Perform descriptive statistics
        print('Descriptive Statistics:')
        print(df.describe())

        # Close the connection
        connection.close()
        print('Connection closed')
        
    else:
        print('Unable to connect to MySQL database')

except Exception as e:
    print('Error:', e)







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

