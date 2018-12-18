#!/usr/bin/python
# coding=utf-8
import xlrd
import chardet
import traceback
def getColumnIndex(table, columnName):
    columnIndex = None
    #print table
    for i in range(table.ncols):
        #print columnName
        #print table.cell_value(0, i)
        if(table.cell_value(0, i) == columnName):
            columnIndex = i
            break
    return columnIndex
def readExcelDataByName(fileName, sheetName):
    #print fileName
    table = None
    errorMsg = ""
    try:
        data = xlrd.open_workbook(fileName)
        table = data.sheet_by_name(sheetName)
    except Exception as msg:
        errorMsg = msg
    return table, errorMsg
def readExcelDataByIndex(fileName, sheetIndex):
    table = None
    errorMsg = ""
    try:
        data = xlrd.open_workbook(fileName)
        table = data.sheet_by_index(sheetIndex)
    except Exception as msg:
        errorMsg = msg
    return table, errorMsg
if __name__ == '__main__':
    #example
    xlsfile= '1.xlsx'
    table = readExcelDataByName(xlsfile, 'Sheet1')[0]


    i = 1
    while (i < table.nrows):

        testcase_id = table.cell_value(i, getColumnIndex(table, "救援号"))


        print ('测试用例ID为：%s'%(testcase_id))
        i+=1
