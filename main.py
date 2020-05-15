# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from token_t_bot import TOKEN
from telegram import ReplyKeyboardMarkup

FLAG = 'user'

main_kb_user = [["Остаток рыб", "Остаток времени", "Мои рыбы"],
                ["Регистрация", "Рыбалка"]]
fish_kb_user = [['Сколько рыб в пруду'], ['Назад']]
time_kb_user = [['Сколько осталось времени'], ['Назад']]
my_fish_kb_user = [['Сколько у меня рыб'], ['Назад']]
reg_kb_user = [['Регистрация'], ['Назад']]
fishing_kb_user = [['Ловить рыбу'], ['Назад']]

main_kb_admin = [["Игра", "Таймер"], ["Статусы"]]
game_kb_admin = [["Начать", "Остановить"], ["Назад"]]
timer_kb_admin = [["Включить таймер (2 мин)"], ["Назад"]]
statuses_kb_admin = [["Остаток времени", "Лог поведения", "Кол-во рыб в пруду"], ["Кол-во рыб в N раунде", "Назад"]]

hmfip_kb_user = [["/how_much_fish_in_pond", "Назад"]]
hmt_kb_user = [["/how_much_time", "Назад"]]
mf_kb_user = [["/my_fish", "Назад"]]
r_kb_user = [["/registration", "Назад"]]
f_kb_user = [['1', "2", "3"], ['Назад']]

sg_kb_admin = [["/start_game", "Назад"]]
stg_kb_admin = [["/stop_game", "Назад"]]
snt_kb_admin = [["/start_new_timer", "Назад"]]
hmt_kb_admin = [["/how_much_time", "Назад"]]
l_kb_admin = [["/log_conduct", "Назад"]]
hmfip_kb_admin = [["/how_much_fish_in_pond", "Назад"]]
hmfir_kb_admin = [["/how_much_fish_in_round", "Назад"]]

# user
markup_main_kb_user = ReplyKeyboardMarkup(main_kb_user, one_time_keyboard=False)
markup_fish_kb_user = ReplyKeyboardMarkup(fish_kb_user, one_time_keyboard=False)
markup_time_kb_user = ReplyKeyboardMarkup(time_kb_user, one_time_keyboard=False)
markup_my_fish_kb_user = ReplyKeyboardMarkup(my_fish_kb_user, one_time_keyboard=False)
markup_reg_kb_user = ReplyKeyboardMarkup(reg_kb_user, one_time_keyboard=False)
markup_fishing_kb_user = ReplyKeyboardMarkup(fishing_kb_user, one_time_keyboard=False)
# admin
markup_main_kb_admin = ReplyKeyboardMarkup(main_kb_admin, one_time_keyboard=False)
markup_game_kb_admin = ReplyKeyboardMarkup(game_kb_admin, one_time_keyboard=False)
markup_timer_kb_admin = ReplyKeyboardMarkup(timer_kb_admin, one_time_keyboard=False)
markup_statuses_kb_admin = ReplyKeyboardMarkup(statuses_kb_admin, one_time_keyboard=False)
# user dop
markup_hmfip_kb_user = ReplyKeyboardMarkup(hmfip_kb_user, one_time_keyboard=False)
markup_hmt_kb_user = ReplyKeyboardMarkup(hmt_kb_user, one_time_keyboard=False)
markup_mf_kb_user = ReplyKeyboardMarkup(mf_kb_user, one_time_keyboard=False)
markup_r_kb_user = ReplyKeyboardMarkup(r_kb_user, one_time_keyboard=False)
markup_f_kb_user = ReplyKeyboardMarkup(f_kb_user, one_time_keyboard=False)
# admin dop
markup_sg_kb_admin = ReplyKeyboardMarkup(sg_kb_admin, one_time_keyboard=False)
markup_stg_kb_admin = ReplyKeyboardMarkup(stg_kb_admin, one_time_keyboard=False)
markup_snt_kb_admin = ReplyKeyboardMarkup(snt_kb_admin, one_time_keyboard=False)
markup_hmt_kb_admin = ReplyKeyboardMarkup(hmt_kb_admin, one_time_keyboard=False)
markup_l_kb_admin = ReplyKeyboardMarkup(l_kb_admin, one_time_keyboard=False)
markup_hmfip_kb_admin = ReplyKeyboardMarkup(hmfip_kb_admin, one_time_keyboard=False)
markup_hmfir_kb_admin = ReplyKeyboardMarkup(hmfir_kb_admin, one_time_keyboard=False)


def how_much_fish_in_pond():
    pass


def how_much_time():
    pass


def my_fish():
    pass


def registration():
    pass


def fishing():
    pass


def start_game():
    pass


def stop_game():
    pass


def start_new_timer():
    pass


def log_conduct():
    pass


def how_much_fish_in_round():
    pass


def send_message(update, context):
    if update.message.text.lower() == "привет":
        update.message.reply_text("Привет, друг! Давай поиграем!")
    elif update.message.text == "Остаток рыб":
        update.message.reply_text("Здесь можно узнать сколько рыб осталосб в пруду", reply_markup=fish_kb_user)
    elif update.message.text == "Сколько рыб в пруду":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=hmfip_kb_user)
    elif update.message.text == "Остаток времени":
        update.message.reply_text("Здесь можно узнать сколько осталось времени", reply_markup=time_kb_user)
    elif update.message.text == "Сколько осталось времени":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=hmt_kb_user)
    elif update.message.text == "Мои рыбы":
        update.message.reply_text("Здесь можно узнать сколько у вас рыб", reply_markup=my_fish_kb_user)
    elif update.message.text == "Сколько у меня рыб":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=mf_kb_user)
    elif update.message.text == "Регистрация":
        update.message.reply_text("Здесь происходит регистрация пользователя", reply_markup=reg_kb_user)
    elif update.message.text == "Регистрация":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=r_kb_user)
    elif update.message.text == "Рыбалка":
        update.message.reply_text("Тут можно ловить рыбку", reply_markup=fishing_kb_user)
    elif update.message.text == "Ловить рыбу":
        update.message.reply_text("Сколько рыб вы хотите поймать???", reply_markup=f_kb_user)
    elif update.message.text == "Назад":
        update.message.reply_text("вас перенесло в главное меню", reply_markup=main_kb_user)
    elif update.message.text.lower() == "привет":
        update.message.reply_text("Привет, друг! Давай поиграем!")
    elif update.message.text == "Игра":
        update.message.reply_text("Управление игрой", reply_markup=game_kb_admin)
    elif update.message.text == "Начать":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=sg_kb_admin)
    elif update.message.text == "Остановить":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=stg_kb_admin)
    elif update.message.text == "Таймер":
        update.message.reply_text("Управление таймером", reply_markup=hmfip_kb_user)
    elif update.message.text == "Включить таймер (2 мин)":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=snt_kb_admin)
    elif update.message.text == "Статусы":
        update.message.reply_text("Управление статусами", reply_markup=statuses_kb_admin)
    elif update.message.text == "Остаток времени":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=hmt_kb_admin)
    elif update.message.text == "Лог поведения":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=l_kb_admin)
    elif update.message.text == "Кол-во рыб в пруду":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=hmfip_kb_admin)
    elif update.message.text == "Кол-во рыб в N раунде":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=hmfir_kb_admin)
    elif update.message.text == "Назад":
        update.message.reply_text("вас перенесло в главное меню", reply_markup=main_kb_admin)



def start(update, context):
    global FLAG
    print(123)
    if FLAG == 'user':
        print(111)
        update.message.reply_text(
            """Привет! Начнём игру!""",
            reply_markup=main_kb_user)
    elif FLAG == 'admin':
        update.message.reply_text(
            """Привет! Начнём игру!""",
            reply_markup=main_kb_admin)


def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater(TOKEN, use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(CommandHandler("start", start))

    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
