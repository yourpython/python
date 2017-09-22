import xlrd


data = xlrd.open_workbook('C:\\Users\\15291\Desktop\\all.xlsx')
table = data.sheet_by_index(0)
print(table.nrows)# row
for i in table.nrows:
  print("第5列所有行数",table.cell(i,2))
