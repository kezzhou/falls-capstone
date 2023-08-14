from .helper import *

""" Question:

=> Compare average number of medications prescribed for patients who have fallen and patients who have not?

"""

class Q2:
    def __init__(self):
        self.helper = Helper()
    
    def start(self):
        # Load the data for patients who have fallen
        df_falls = pd.read_csv('./data/original/medication_drug_falls.csv')

        # Load the data for patients who have not fallen
        df_non_falls = pd.read_csv('./data/original/medication_drug.csv')

        # Calculate the average number of medications for both groups
        avg_medications_falls = df_falls['patient_id'].value_counts().mean()
        avg_medications_non_falls = df_non_falls['patient_id'].value_counts().mean()

        # Create a bar chart to compare the averages
        self.helper.display_bar_chart(
            index=['Falls', 'Non-Falls'],
            values=[avg_medications_falls, avg_medications_non_falls],
            title='Average Number of Medications Prescribed',
            xlabel='Patient Group',
            ylabel='Average Number of Medications',
            export_loc='insights/q2__average_medications.png',
            bar_width=0.3
        )
        self.after_completion()
    
    def after_completion(self):
        print("Q2 Completed.")

