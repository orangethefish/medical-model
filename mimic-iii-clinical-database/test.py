import pandas as pd

# Load the DIAGNOSES_ICD.csv file
diagnosis_df = pd.read_csv('DIAGNOSES_ICD.csv')

# Ensure the ICD codes column is provided as a string for correct comparison
diagnosis_df['icd9_code'] = diagnosis_df['icd9_code'].astype(str)

# Filter hypertensive patients with ICD codes between 401 and 405
hypertensive_patients = diagnosis_df.loc[
    (diagnosis_df['icd9_code'] >= '401') & (diagnosis_df['icd9_code'] <= '405')
].copy()

#Add column label 1
hypertensive_patients['label'] = 1


# Filter non-hypertensive patients (those outside the ICD codes 401-405 range)
non_hypertensive_patients = diagnosis_df.loc[
    (diagnosis_df['icd9_code'] < '401') | (diagnosis_df['icd9_code'] > '405')
].copy()

# Add column label 0
non_hypertensive_patients['label'] = 0


# Balance the dataset by sampling
# You may adjust the number of samples based on your dataset and requirements
non_hypertensive_sample = non_hypertensive_patients.sample(n=len(hypertensive_patients))

merged_df = pd.concat([hypertensive_patients, non_hypertensive_sample])

# Load the PATIENTS.csv file
patients_df = pd.read_csv('PATIENTS.csv')

merged_df['subject_id'] = merged_df['subject_id'].astype(patients_df['subject_id'].dtype) 

merged_patient_info = pd.merge(merged_df, patients_df[['subject_id', 'gender']], on='subject_id', how='left')

merged_patient_info =  merged_patient_info[['subject_id', 'gender', 'label']]
print(merged_patient_info)

