import xlsxwriter


def create_table(table_name):
    workbook = xlsxwriter.Workbook(table_name)
    worksheet = workbook.add_worksheet()
    data = [('Развлечения', 6800), ('Продукты', 25670), ('Транспорт', 3450), ]

    for row, (item, price) in enumerate(data):
        worksheet.write(row, 0, item)
        worksheet.write(row, 1, price)

    row += 1
    worksheet.write(row, 0, 'Всего')
    worksheet.write(row, 1, '=SUM(B1:B3)')

    workbook.close()


create_table('qwee.xlsx')
