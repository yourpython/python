#!python3
#coding:utf-8

import openpyxl,uniout,pprint
print (u'打开 表格····')
wb = openpyxl.load_workbook(u'梅县1.xlsx')
sheet = wb.get_sheet_by_name(u'梅县')
nameData = {}
print (u'读取中····')
for row in range(2,len(list(sheet.rows))):
        #v从行2到有数据的行尾
        state = sheet['u'+str(row)].value #各县的值
        name  = sheet['b'+str(row)].value #姓名
        count  = sheet['n'+str(row)].value #医疗费总额
        bj = sheet['ab'+str(row)].value #特殊人员标记
        ID = sheet['d'+str(row)].value
print type(count)
print len(list(sheet.rows))
#for row in range(2,len(list(sheet.rows))):
