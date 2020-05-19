import xlsxwriter
from register_func import get_name_playing

workbook = xlsxwriter.Workbook("qwee1.xlsx")
worksheet = workbook.add_worksheet()
round_game = 1


def create_table(table_name):
    global workbook, worksheet, round_game
    workbook = xlsxwriter.Workbook(table_name)
    worksheet = workbook.add_worksheet()
    round_game = 1
    data = ['Игрок'] + get_name_playing() + ['Пруд']

    for row, name_user in enumerate(data):
        worksheet.write(row, 0, name_user)
    return get_name_playing()


def save_data(data, all_fish):
    global round_game
    worksheet.write(0, round_game, str(round_game) + " Раунд")
    for row, fish in enumerate(data):
        worksheet.write(row + 1, round_game, fish)
    worksheet.write(row + 2, round_game, all_fish)
    round_game += 1

def close_table():
    workbook.close()