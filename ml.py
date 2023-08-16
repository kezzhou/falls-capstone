# ML Predictions

from src.s1 import PredictFalls
from src.s2 import PredictReadmission

# Scenario 1

medication_code = "1116294"
pf = PredictFalls(medication_code)
accuracy, precision, recall, conf_matrix = pf.train()

# # Print the results
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"Confusion Matrix:\n{conf_matrix}")

new_medication_data_path = './medication_drug_falls.csv'
new_encounter_data_path = './encounter_falls.csv'
pf.predict_new_data(new_medication_data_path, new_encounter_data_path)

# Scenario 2

diagnosis_code = "C18.7"
pr = PredictReadmission(diagnosis_code)
pr.train()
new_diagnosis_data_path = "./diagnosis_falls.csv"
new_encounter_data_path = "./encounter_falls.csv"
pr.predict_new_data(new_diagnosis_data_path, new_encounter_data_path)
