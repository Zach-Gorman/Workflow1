import os
import pandas as pd

df = pd.read_csv('ModelCleaning/data.csv')

print("Original Data:")
print(df.head())

df.columns = df.columns.str.strip()

df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
df = df.map(lambda x: x.lower() if isinstance(x, str) else x)

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

workspace = os.getenv('GITHUB_WORKSPACE')
model_cleaning_dir = os.path.join(workspace, 'ModelCleaning')
output_path = os.path.join(model_cleaning_dir, 'cleaned_data.csv')

os.makedirs(model_cleaning_dir, exist_ok=True)

df.to_csv(output_path, index=False)

print(output_path)
print("Cleaned Data:")
print(df.head())

print("\nCleaned data saved to 'cleaned_data.csv'")