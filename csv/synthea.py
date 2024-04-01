import pandas as pd

# Load datasets
allergies_df = pd.read_csv('allergies.csv')
careplans_df = pd.read_csv('careplans.csv')
conditions_df = pd.read_csv('conditions.csv')
encounters_df = pd.read_csv('encounters.csv')
immunizations_df = pd.read_csv('immunizations.csv')
medications_df = pd.read_csv('medications.csv')
procedures_df = pd.read_csv('procedures.csv')
observations_df = pd.read_csv('observations.csv')
patients_df = pd.read_csv('patients.csv')
payer_transitions_df = pd.read_csv('payer_transitions.csv')

# Now, let's select specific features from each DataFrame
# For instance:

# Selecting from Allergies
allergies_features = allergies_df[['START', 'STOP', 'PATIENT', 'CODE']]

# Selecting from Careplans
careplans_features = careplans_df[['START', 'STOP', 'PATIENT', 'CODE', 'REASONCODE']]

# Selecting from Conditions
conditions_features = conditions_df[['START', 'STOP', 'PATIENT', 'CODE']]

# Selecting from Encounters
encounters_features = encounters_df[['START', 'STOP', 'PATIENT', 'ENCOUNTERCLASS', 'CODE', 'REASONCODE']]

# Selecting from Immunizations
immunizations_df = immunizations_df[['DATE', 'PATIENT', 'CODE']]

# Selecting from Medications
medications_features = medications_df[['START', 'STOP', 'PATIENT', 'CODE', 'REASONCODE']]

# Selecting from Procedures
procedures_features = procedures_df[['DATE', 'PATIENT', 'CODE', 'REASONCODE']]

# Selecting from Observations
observations_features = observations_df[['DATE', 'PATIENT', 'CODE', 'VALUE', 'UNITS']]

# Selecting from Patients
patients_features = patients_df[['BIRTHDATE', 'DEATHDATE', 'ETHNICITY','GENDER']]

# Selecting from Payer Transitions
patients_transitions_features = payer_transitions_df[['START_YEAR', 'END_YEAR', 'PATIENT']]

from functools import reduce

# List of datasets to merge
dataframes = [allergies_features, careplans_features, conditions_features, encounters_features]

# Initialize an empty list to store the merged DataFrames with suffixes
merged_dataframes = []

# Loop through the list of DataFrames and merge them into a single DataFrame with custom suffixes
for i, df in enumerate(dataframes):
    if i == 0:
        # The first DataFrame doesn't need to be merged with anything,
        # so just add it to the list
        merged_dataframes.append(df)
    else:
        # Merge the current DataFrame with the last one in the merged list
        # Specify appropriate suffixes to avoid column name duplications
        merged_df = pd.merge(merged_dataframes[-1], df, on='PATIENT', how='outer', suffixes=('', f'_df{i}'))
        merged_dataframes.append(merged_df)

# The last item in the merged_dataframes list is the fully merged DataFrame
full_patient_data = merged_dataframes[-1]

print(full_patient_data.head())