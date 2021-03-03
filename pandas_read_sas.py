import pandas as pd


sas_file = r'C:\temp\my_sas_file.sas7bdat'
df = pd.read_sas(sas_file, format='sas7bdat', encoding='latin-1')
