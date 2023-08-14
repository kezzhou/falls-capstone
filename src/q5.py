from .helper import *

""" Question:

=> What are the most common lab results for patients who have fallen?

"""

class Q5:
    def __init__(self):
        self.helper = Helper()
    
    def start(self):
        # Load the data for patients who have fallen
        df_falls = pd.read_csv('./data/original/lab_result_falls.csv')

        # Change as per need
        number_of_lab_results = 7

        # Get the top n lab results for patients who have fallen
        top_lab_results = df_falls['code'].value_counts().nlargest(number_of_lab_results)

        # Create a bar chart of the top n lab results for patients who have fallen
        self.helper.display_bar_chart(
            index=top_lab_results.index,
            values=top_lab_results.values,
            title=f'Top {number_of_lab_results} Lab Results for Patients Who Have Fallen',
            xlabel='Lab Result Code',
            ylabel='Number of Occurrences',
            export_loc='insights/q5__top_lab_results.png'
        )
        self.after_completion()
    
    def after_completion(self):
        print("Q5 Completed.")

