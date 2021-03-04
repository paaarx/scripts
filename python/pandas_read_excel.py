# pip install - U pandas
# pip install - U xlrd
# pip install - U openpyxl
import pandas as pd


xlsx_file = r'C:\python_project\code\sample.xlsx'
df = pd.read_excel(xlsx_file, sheet_name='Sheet1', header=0, usecols='A:B')

print(df.head(5))
