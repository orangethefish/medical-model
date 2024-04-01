import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from datetime import datetime

df = pd.read_csv('mimic-iii-clinical-database/ADMISSIONS.csv')
# Calculate age at the time of admission
df['admittime'] = pd.to_datetime(df['admittime'])
df['dob'] = pd.to_datetime(df['dob'])
df['age'] = (df['admittime'] - df['dob']).dt.days / 365.25

# Calculate Length of Stay (LOS) and drop admittime and dischtime
df['dischtime'] = pd.to_datetime(df['dischtime'])
df['LOS'] = (df['dischtime'] - df['admittime']).dt.total_seconds() / (24 * 60 * 60)
df.drop(['hadm id', 'subject id', 'admittime', 'dischtime', 'dob'], axis=1, inplace=True)

# Feature selection - assuming these are the columns remaining after dropping identifiers
categorical_cols = ['ethnicity', 'admission type', 'admission location', 'insurance', 'religion', 'marital status', ...]
numerical_cols = ['age', 'LOS']  # Include other numerical columns you may have

# One-hot encode categorical variables
encoder = OneHotEncoder(sparse=False)
encoded_categorical = encoder.fit_transform(df[categorical_cols])
categorical_df = pd.DataFrame(encoded_categorical, columns=encoder.get_feature_names(categorical_cols))

# Combine numerical and encoded categorical data
final_df = pd.concat([df[numerical_cols].reset_index(drop=True), categorical_df], axis=1)