import pandas as pd
import os

reader = pd.read_excel(os.path.join("excel/sheets.xlsx"), engine='openpyxl', sheet_name=None)
for key in reader.keys():
sheet = pd.read_excel("excel/sheets.xlsx", engine='openpyxl', sheet_name=key)
sheet.to_csv(f"{key}.csv")


