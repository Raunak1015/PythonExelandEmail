import openpyexcel
path="D:/testData.xlsx"
workbook=openpyexcel.load_workbook(path)
sheet=workbook.get_sheet_by_name("Sheet2")

for r in range(1,5):
    for c in range(1,5):
        sheet.cell(row=r,column=c).value="Hello"

workbook.save(path)


