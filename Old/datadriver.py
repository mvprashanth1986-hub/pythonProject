from Old import XLUtils

file = "C:\pythonutils\AccountInfo1.xlsx"


row = XLUtils.row_count(file, 'Sheet1')
col = XLUtils.col_count(file, 'Sheet1')


for r in range(2,row+1):
        XLUtils.write_date(file, 'Sheet1', r, 4, "tttt")