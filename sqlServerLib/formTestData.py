# author: ~E酱

import openpyxl as op
import random as rd

workbook = op.Workbook()
sheet = workbook.active

sheet['A1'] = '姓名'
sheet['B1'] = '字符串测试'
sheet['C1'] = '整形测试'
sheet['D1'] = '长数字测试'
sheet['E1'] = '定长浮点型测试'
sheet['F1'] = '任意浮点型测试'

uab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lab = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
a = uab + lab +num
b = uab + lab

def formRdStr(ab, maxLen = 20):
    s = ''
    for i in range(rd.randint(1, maxLen)):
        s += ab[rd.randint(0, len(ab) - 1)]
    return s

for i in range(2, 1001):
    sheet['A' + str(i)] = formRdStr(a)
    sheet['B' + str(i)] = formRdStr(b)
    sheet['C' + str(i)] = rd.randint(1, 1000000)
    sheet['D' + str(i)] = int(formRdStr(num, 10))
    sheet['E' + str(i)] = rd.randint(1, 1000000000000) / 100
    sheet['F' + str(i)] = float(formRdStr(num, 10) + '.' + formRdStr(num))

workbook.save('test.xlsx')



