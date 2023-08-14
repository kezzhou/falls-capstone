from .helper import *

""" Question:

=> Which medications has been prescribed most frequently to fall patients?

"""

class Q6:
    def __init__(self):
        self.helper = Helper()
    
    def start(self):
        # Load the data for patients who have fallen
        df_diagnosis_falls = pd.read_csv('./data/original/diagnosis_falls.csv')
        df_encounter_falls = pd.read_csv('./data/original/encounter_falls.csv')
        # Load the terminology mapping and specify the data type for the 'code' column
        df_terminology_falls = pd.read_csv('./data/original/standardized_terminology_falls.csv', dtype={'code': str}, low_memory=False)  # Load the terminology mapping

        # Merge the terminology mapping with the diagnosis data
        df_diagnosis_falls = pd.merge(df_diagnosis_falls, df_terminology_falls, left_on='code', right_on='code')

        # Change as per need
        top_n_diseases = 5

        # Get the top N diagnosis codes for patients who have fallen
        top_diagnosis_codes = df_diagnosis_falls['code_description'].value_counts().nlargest(top_n_diseases).index

        # Merge diagnosis and encounter data on patient_id and encounter_id
        merged_data = pd.merge(df_diagnosis_falls, df_encounter_falls, on=['patient_id', 'encounter_id'])

        # Filter the data for the top N diagnosis codes
        filtered_data = merged_data[merged_data['code_description'].isin(top_diagnosis_codes)].copy()

        # Convert start_date and end_date to datetime
        filtered_data['start_date'] = pd.to_datetime(filtered_data['start_date'], format='%Y%m%d')
        filtered_data['end_date'] = pd.to_datetime(filtered_data['end_date'], format='%Y%m%d')

        # Calculate the length of stay
        filtered_data['length_of_stay'] = (filtered_data['end_date'] - filtered_data['start_date']).dt.days

        # Calculate the average length of stay for each diagnosis code
        avg_length_of_stay = filtered_data.groupby('code_description')['length_of_stay'].mean()

        # Create a bar chart of the average length of stay for the top N diseases
        self.helper.display_bar_chart(
            index=avg_length_of_stay.index,
            values=avg_length_of_stay.values,
            title=f'Average Length of Stay for Top {top_n_diseases} Diseases in Fall Patients',
            xlabel='Disease Name',
            ylabel='Average Length of Stay (days)',
            export_loc='insights/q6__avg_length_of_stay.png'
        )
        self.after_completion()
    
    def after_completion(self):
        print("Q6 Completed.")

