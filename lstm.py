import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split


admissions = pd.read_csv('mimic-iii-clinical-database/ADMISSIONS.csv')
patients = pd.read_csv('mimic-iii-clinical-database/PATIENTS.csv')
icu_stays = pd.read_csv('mimic-iii-clinical-database/ICUSTAYS.csv')

admissions = admissions.dropna(axis = 0, how ='any')
