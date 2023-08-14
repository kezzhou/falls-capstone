from .helper import *

""" Question:

=> What are the most common medications prescribed for patients who have fallen?

"""

class Q3:
    def __init__(self):
        self.helper = Helper()
    
    def start(self):
        # Load the data for patients who have fallen
        df_falls = pd.read_csv('./data/original/medication_drug_falls.csv')

        # Change as per need
        number_of_medications = 7

        # Get the top n medications for patients who have fallen
        top_medications = df_falls['code'].value_counts().nlargest(number_of_medications)

        # Create a bar chart of the top n medications for patients who have fallen
        self.helper.display_bar_chart(
            index=top_medications.index,
            values=top_medications.values,
            title=f'Top {number_of_medications} Medications Prescribed for Patients Who Have Fallen',
            xlabel='Medication Code',
            ylabel='Number of Prescriptions',
            export_loc='insights/q3__top_medications.png'
        )
        self.after_completion()
    
    def after_completion(self):
        print("Q3 Completed.")
