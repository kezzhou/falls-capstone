from .helper import *

""" Question:

=> Which diagnosis code has been assigned most frequently to fall patients, and non-fall patients?

"""

class Q7:
    def __init__(self):
        self.helper = Helper()
    
    def start(self):
        # Load the data for patients who have fallen
        df_falls = pd.read_csv('./data/diagnosis_falls.csv')
        # Load the data for patients who have not fallen
        df_non_falls = pd.read_csv('./data/diagnosis.csv')

        # Get the most frequent diagnosis code for patients who have fallen
        top_diagnosis_falls = df_falls['code'].value_counts().nlargest(1)
        # Get the most frequent diagnosis code for patients who have not fallen
        top_diagnosis_non_falls = df_non_falls['code'].value_counts().nlargest(1)

        # Combine the results
        labels = [f'Fall Patients\n{top_diagnosis_falls.index[0]}', f'Non-Fall Patients\n{top_diagnosis_non_falls.index[0]}']
        sizes = [top_diagnosis_falls.values[0], top_diagnosis_non_falls.values[0]]

        # Create a pie chart
        self.helper.display_pie_chart(
            labels=labels,
            sizes=sizes,
            title='Most Frequent Diagnosis Codes',
            export_loc='insights/q7__top_diagnosis_codes.png',
            display_percentage=True
        )
        self.after_completion()
    
    def after_completion(self):
        print("Q7 Completed.")
