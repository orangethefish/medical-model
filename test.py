import numpy as pd 
import pandas as pd

patients = pd.read_csv('mimic-iii-clinical-database/PATIENTS.csv')

#calculate the mean of the ages using dod and dob
patients['dob'] = pd.to_datetime(patients['dod'])
patients['dod'] = pd.to_datetime(patients['dod'])

patients['age'] = (patients['dod'] - patients['dob']).dt.days/365.25

print(patients['age'])