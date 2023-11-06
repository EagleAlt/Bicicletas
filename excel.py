import openpyxl as xl

book = xl.load_workbook('usuarios.xlsx')
sheet = book.active

for i in range(2, sheet.max_row):
     print(type(sheet[f'E{i}'].value))

