from .helper import *

""" Question:

=> What is the distribution of encounter types (AMB, IMP, SS) for patients who have fallen?

"""

class Q4:
    def __init__(self):
        self.helper = Helper()
    
    def start(self):
        # Load the data for patients who have fallen
        df_falls = pd.read_csv('./data/original/encounter_falls.csv')

        # Get the distribution of encounter types
        encounter_types_distribution = df_falls['type'].value_counts()

        # Filter only the required types (AMB, IMP, SS)
        encounter_types_distribution = encounter_types_distribution.loc[['AMB', 'IMP', 'SS']]

        # Create a pie chart of the distribution of encounter types
        self.helper.display_pie_chart(
            labels=encounter_types_distribution.index,
            sizes=encounter_types_distribution.values,
            title='Distribution of Encounter Types for Patients Who Have Fallen',
            export_loc='insights/q4__encounter_distribution_pie.png',
            display_percentage=False
        )
        self.after_completion()
    
    def after_completion(self):
        print("Q4 Completed.")
