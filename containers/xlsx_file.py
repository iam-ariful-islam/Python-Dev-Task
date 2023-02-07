import xlsxwriter


# create xlsx file using xlsxwriter
def create_xlsx_file(fname, data):
    workbook  = xlsxwriter.Workbook(fname)
    worksheet = workbook.add_worksheet()

    for i, (key, value) in enumerate(data.items()):
        worksheet.write(i, 0, key)
        worksheet.write(i, 1, value)
        
    workbook.close()