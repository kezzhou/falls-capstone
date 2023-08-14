# Southampton Hospital Falls
Stony Brook Applied Health Informatics - Capstone Project

## Overview:

Falls are a significant concern in healthcare settings, especially among elderly patients and those with specific health conditions. Falls can result in severe injuries, prolonged hospital stays, increased healthcare costs, and a decline in patients' overall well-being. They are considered a leading cause of morbidity and mortality, highlighting the importance of preventive measures.

By conducting a capstone project focused on identifying predictors of falls, valuable insights can be gained to enhance fall risk assessment and prevention strategies.

By understanding the factors that contribute to falls, healthcare professionals can implement targeted interventions such as:
- improved patient monitoring
- environmental modifications
- tailored patient education

The primary objective of this capstone project is to investigate and analyze the relationship between medical & treatment regimens and falls readmissions. By leveraging both falls & non-fall patient datasets, this project aims to uncover significant correlations and patterns related to falls. The project seeks to utilize advanced data analysis techniques, including exploratory data analysis, statistical modeling, and predictive analytics, to develop a robust understanding of the factors contributing to falls. Ultimately, the findings of this capstone project will inform the development of targeted fall prevention strategies, interventions, and protocols, enhancing patient safety and improving the quality of care provided within the hospital.


What you'll find in this repository:
1. data folder
2. data dictionary
3. insights folder
4. documents folder
5. scripts folder
6. README.md
7. requirements.txt


## Resources:

[TriNetX DeIdentified Patient Database](https://trinetx.com/)

## Requirements:

- Visual Studio Code/Platform of Choice
- MySqlWorkbench
- Jupyter Notebooks/Google Colab
- Tableau

## Notes:

Please refer to the documents folder for documentation of project planning.

Querying datasets from TriNetX requires an organization email, which unfortunately I did not apply for at the start of the project because of its long processing time. 

Currently working through problems with pushing data into mysqlworkbench. For now I've opted to use the CSVs directly for analysis and visualization. 

Even the falls patients don't seem to have falls as their primary diagnosis, which is strange and interferes with easy identification of falls patients.

Considering trying a query for patients with at least two diagnoses of falls less than 30 days apart or looking for encounter types of HH (Health Home).