import pandas as pd
path = r'c:\Users\Zarak\OneDrive - Higher Education Commission\Desktop\MLOPS\diabetes_unclean.csv'
df = pd.read_csv(path)
print(df.dtypes)
print('----')
print([col for col in df.columns if df[col].dtype != 'object' and not pd.api.types.is_numeric_dtype(df[col])])
