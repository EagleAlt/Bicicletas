import openpyxl as xl

book = xl.Workbook()
sheet = book.active

sheet['A1'] = "Nombre"
sheet['A2'] = "Apellido"

sheet

book.save('usuarios.xlsx')

