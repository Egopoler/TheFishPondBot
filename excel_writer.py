import xlsxwriter
from register_func import get_name_playing


def create_table(table_name):
    workbook = xlsxwriter.Workbook(table_name)
    worksheet = workbook.add_worksheet()
    data = ['Игрок'] + get_name_playing() + ['Пруд']

    for row, name_user in enumerate(data):
        worksheet.write(row, 0, name_user)

    row += 1
    workbook.close()


create_table('qwee.xlsx')