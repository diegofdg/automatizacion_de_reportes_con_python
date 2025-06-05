import pandas as pd
import openpyxl

archivo_excel = pd.read_excel('project-report/supermarket_sales.xlsx')
# print(archivo_excel[['Gender', 'Product line', 'Total']])

table_pivote = archivo_excel.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)
print(table_pivote)

table_pivote.to_excel('sales_2022.xlsx', startrow=4, sheet_name='Report')