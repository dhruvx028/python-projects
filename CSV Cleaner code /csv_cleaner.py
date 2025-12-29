import pandas as pd
df = pd.read_csv("FILES/csv_files/data.csv")
df = df.drop_duplicates()
df = df.dropna()
df = df.to_csv("FILES/csv_files/cleaned_data.csv")
df = None

print("CSV file cleaned and saved as 'cleaned_data.csv'")   
