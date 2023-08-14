from .helper import *

""" Question:

=> What is the most common diagnosis code for patients who have fallen?

"""

class Q1:
    def __init__(self):
        self.helper = Helper()
    
    def start(self):
        # Load the diagnosis_falls.csv file
        df = pd.read_csv('./data/original/diagnosis_falls.csv')

        # Change as per need
        number_of_diagnosis_codes = 7

        # Get the top n diagnosis codes for patients who have fallen
        top_diagnosis_codes = df['code'].value_counts().nlargest(number_of_diagnosis_codes)

        # Create a bar chart of the top n diagnosis codes for patients who have fallen
        self.helper.display_bar_chart(
            index=top_diagnosis_codes.index,
            values=top_diagnosis_codes.values,
            title=f'Top {number_of_diagnosis_codes} Diagnosis Codes for Patients Who Have Fallen',
            xlabel='Diagnosis Code',
            ylabel='Number of Patients',
            export_loc='insights/q1__top_diagnosis_codes.png'
        )
        self.after_completion()
    
    def after_completion(self):
        print("Q1 Completed.")


