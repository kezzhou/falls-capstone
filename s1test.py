import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data from CSV files into pandas DataFrames
medication_drug = pd.read_csv('./data/original/medication_drug.csv')
encounter = pd.read_csv('./data/original/encounter.csv')
patient = pd.read_csv('./data/original/patient.csv')

# Merge DataFrames on patient_id with specified suffixes
df = pd.merge(medication_drug[medication_drug['code'] == 1116294], encounter, on='patient_id', suffixes=('_medication', '_encounter'))
df = pd.merge(df, patient, on='patient_id')

# Rename the 'start_date_medication' column to 'start_date'
df.rename(columns={'start_date_medication': 'start_date'}, inplace=True)

# Preprocess data
df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])
df['fall_in_60_days'] = (df['end_date'] - df['start_date']).dt.days.le(60)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[['code', 'start_date']], df['fall_in_60_days'], test_size=0.2)

# Train decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Evaluate performance of classifier on testing set
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Predict likelihood of patients on 1116294 medication falling in next 60 days
new_data = pd.DataFrame({'value': [200], 'start_date': ['2023-08-15']})
new_data['start_date'] = pd.to_datetime(new_data['start_date'])
new_data_pred = clf.predict(new_data)
print(f'Predicted likelihood of falling in next 60 days: {new_data_pred[0]}')
