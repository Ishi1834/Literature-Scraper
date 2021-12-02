import xlsxwriter

def initiate_spreedsheet(keywords):
    workbook = xlsxwriter.Workbook('articles.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0,0,'Title')
    worksheet.write(0,1,'Description')
    worksheet.write(0,2,'Link')
    worksheet.write(0,3,'Citations')
    worksheet.write(0,4,'Related articles')
    worksheet.write(0,5,'Keyword ranking')
    column = 6
    for keyword in keywords:
        worksheet.write(0,column,keyword)
        column = column + 1
    return worksheet, workbook