from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler

import excel_writer
from token_t_bot import TOKEN
from register_func import check_name, check_password, register_flag, add_user, change_game_code, get_name_for_id, \
    check_Admin, change_Admin, check_register, close_register, open_register, check_game_code, get_ids_playing, \
    clear_game
from telegram import ReplyKeyboardMarkup
from excel_writer import create_table, save_data, fish_pond, fish_pond_now, get_fishes, del_fishes, \
    change_fish_pond_now, edit_fish_pond, return_round
from fish_func import get_fish, del_fish, check_fish, check_life, breeding, caught_all_in_round, caught_in_round, \
    fish_flag_check, caught_check, fish_flag_open, get_caught_from_db, erease_caught, fish_flag_close
from log_in_game import create_log_file, add_line

main_kb_user = [["Остаток рыб", "Остаток времени", "Мои рыбы"],
                ["Регистрация", "Рыбалка"]]
fish_kb_user = [['Сколько рыб в пруду'], ['Назад']]
time_kb_user = [['Сколько осталось времени'], ['Назад']]
my_fish_kb_user = [['Сколько у меня рыб'], ['Назад']]
reg_kb_user = [['Регистрация игрока'], ['Назад']]
fishing_kb_user = [['Ловить рыбу'], ['Назад']]

main_kb_admin = [["Игра", "Таймер"], ["Статусы"]]
game_kb_admin = [["Начать", "Остановить"], ["Назад <-"]]
timer_kb_admin = [["Включить таймер (2 мин)"], ["Назад <-"]]
statuses_kb_admin = [["Остаток времени", "Лог поведения", "Кол-во рыб в пруду"], ["Кол-во рыб в N раунде", "Назад <-"]]

hmfip_kb_user = [["/how_much_fish_in_pond", "Назад"]]
hmt_kb_user = [["/how_much_time", "Назад"]]
mf_kb_user = [["/my_fish", "Назад"]]
r_kb_user = [["/register", "Назад"]]
f_kb_user = [['/fishing'], ['Назад']]

sg_kb_admin = [["/start_game", "Назад <-"]]
stg_kb_admin = [["/stop_game", "Назад <-"]]
snt_kb_admin = [["/start_new_timer", "Назад <-"]]
hmt_kb_admin = [["/how_much_time", "Назад <-"]]
l_kb_admin = [["/log_conduct", "Назад <-"]]
hmfip_kb_admin = [["/how_much_fish_in_pond", "Назад <-"]]
hmfir_kb_admin = [["/how_much_fish_in_round", "Назад <-"]]

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

user_table_list = []


def how_much_fish_in_pond(update, context):
    if update.message.chat.id in get_ids_playing() or check_Admin(update.message.chat.id):
        fishes = get_fishes()
        update.message.reply_text(fishes)


def how_much_time():
    pass


def my_fish(update, context):
    if update.message.chat.id in get_ids_playing():
        name = get_name_for_id(update.message.chat.id)
        update.message.reply_text(check_fish(name))


def fishing(update, context):
    if update.message.chat.id in get_ids_playing():
        update.message.reply_text("""Напишите количество рыб, которое вы хотите поймать от 0 до 3.
Вы не можете поймать больше рыбы, чем есть в пруду.
Если вы хотите прервать диалог напишите Стоп. """)
        return 1
    else:
        return ConversationHandler.END


def fishing1(update, context):
    fish_pond_now = get_fishes()
    if update.message.text.lower() == "стоп":
        update.message.reply_text("Вы прервали диалог")
        return ConversationHandler.END
    try:
        fish = int(update.message.text)
        name = get_name_for_id(update.message.chat.id)
        caught = caught_check(update.message.chat.id)
        flag = fish_flag_check()
        if caught or not flag:
            update.message.reply_text('Вы сейчас не можете ловить рыбу')
            return ConversationHandler.END
        elif fish <= 3 and fish >= 0 and fish <= fish_pond_now:
            get_fish(name, fish)
            caught_in_round(update.message.chat.id, fish)
            del_fishes(fish)
            print(fish_pond_now)
            update.message.reply_text(f'Вы поймали {fish} рыбы')
            add_line(f"{name} поймал {fish} рыб")
            return ConversationHandler.END
        else:
            update.message.reply_text("Нужно ввести число от 0 до 3, которое не должно превышать кол-во рыб в пруду")
    except Exception:
        update.message.reply_text("Нужно ввести число от 0 до 3, которое не должно превышать кол-во рыб в пруду")


def stop_game(update, context):
    if check_Admin(update.message.chat.id):
        print(1)
        excel_writer.close_table()
        doc = open("game_table.xlsx", "rb")
        context.bot.send_document(update.message.chat.id, doc)
        close_register()
        fish_flag_close()
        clear_game()
        ids = get_ids_playing()
        for id in ids:
            context.bot.send_message(id, text='Игра закончилась. Рыб не осталось!')


def start_new_timer(update, context):
    chat_id = update.message.chat_id
    due = 3
    if 'job' in context.chat_data:
        old_job = context.chat_data['job']
        old_job.schedule_removal()
    new_job = context.job_queue.run_once(task, due, context=chat_id)
    context.chat_data['job'] = new_job
    update.message.reply_text(f"""Таймер установлен. Две минуты начались.""")


def task(context):
    job = context.job
    context.bot.send_message(job.context, text='Дзинь-Дзинь! Раунд закончился!')
    all_fish = excel_writer.get_fishes_start()[-1]
    save_data(user_table_list, all_fish)


def fake_task(update, context):
    all_fish = excel_writer.get_fishes_start()[-1]
    save_data(get_caught_from_db(user_table_list), all_fish)
    print('yes')
    fish_flag_close()
    #  excel_writer.close_table()
    erease_caught(user_table_list)
    for name in user_table_list:
        del_fish(name)
        if not check_life(name):
            change_game_code(None, name)
            add_line(f"{name} умер")
    if excel_writer.check_fish_pond_now:
        ids = get_ids_playing()
        for id in ids:
            context.bot.send_message(id, text='Игра закончилась. Рыб не осталось!')
        excel_writer.close_table()
        doc = open("game_table.xlsx", "rb")
        context.bot.send_document(update.message.chat.id, doc)
        close_register()
        fish_flag_close()
        clear_game()


def rounds(update, context):
    global user_table_list
    if check_Admin(update.message.chat.id):
        fishes = get_fishes()
        fishes = breeding(fishes)
        edit_fish_pond(fishes)
        change_fish_pond_now()
        fish_flag_open()
        ids = get_ids_playing()
        add_line(f"{return_round()} Раунд")
        for id in ids:
            context.bot.send_message(id, text=f'Начался {return_round()} раунд! в пруду {fishes} рыб')
    else:
        update.message.reply_text("Только Администратор может пользоваться данной командой")
        return ConversationHandler.END


def log_conduct(update, context):
    doc = open("log.txt", "rb")
    context.bot.send_document(update.message.chat.id, doc)


def how_much_fish_in_round(update, context):
    if check_Admin(update.message.chat.id):
        update.message.reply_text("""Напишите номер раунда в котором вы хотите узнать количество рыб.
Если вы хотите прервать диалог напишите Стоп.""")
        return 1
    else:
        update.message.reply_text("Только Администратор может пользоваться данной командой")
        return ConversationHandler.END


def how_much_fish_in_round1(update, context):
    if update.message.text.lower() == "стоп":
        update.message.reply_text("Вы прервали диалог")
        return ConversationHandler.END
    try:
        round_ = int(update.message.text)
        if round_ <= return_round():
            update.message.reply_text(excel_writer.get_fishes_start()[round_ - 1])
            return ConversationHandler.END
        else:
            update.message.reply_text("По данному раунду нет информации")
            return ConversationHandler.END
    except Exception:
        update.message.reply_text("""Напишите номер раунда в котором вы хотите узнать количество рыб.
Если вы хотите прервать диалог напишите Стоп.""")


def send_message(update, context):
    if update.message.text.lower() == "привет":
        update.message.reply_text("Привет, друг! Давай поиграем!")
    elif update.message.text == "Остаток рыб":
        update.message.reply_text("Здесь можно узнать сколько рыб осталосб в пруду", reply_markup=markup_fish_kb_user)
    elif update.message.text == "Сколько рыб в пруду":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=markup_hmfip_kb_user)
    elif update.message.text == "Остаток времени":
        update.message.reply_text("Здесь можно узнать сколько осталось времени", reply_markup=markup_time_kb_user)
    elif update.message.text == "Сколько осталось времени":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=markup_hmt_kb_user)
    elif update.message.text == "Мои рыбы":
        update.message.reply_text("Здесь можно узнать сколько у вас рыб", reply_markup=markup_my_fish_kb_user)
    elif update.message.text == "Сколько у меня рыб":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=markup_mf_kb_user)
    elif update.message.text == "Регистрация":
        update.message.reply_text("Здесь происходит регистрация пользователя", reply_markup=markup_reg_kb_user)
    elif update.message.text == "Регистрация игрока":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=markup_r_kb_user)
    elif update.message.text == "Рыбалка":
        update.message.reply_text("Тут можно ловить рыбку", reply_markup=markup_fishing_kb_user)
    elif update.message.text == "Ловить рыбу":
        update.message.reply_text("Сколько рыб вы хотите поймать???", reply_markup=markup_f_kb_user)
    elif update.message.text == "Назад":
        update.message.reply_text("вас перенесло в главное меню", reply_markup=markup_main_kb_user)
    elif update.message.text.lower() == "привет":
        update.message.reply_text("Привет, друг! Давай поиграем!")
    elif update.message.text == "Игра":
        update.message.reply_text("Управление игрой", reply_markup=markup_game_kb_admin)
    elif update.message.text == "Начать":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=markup_sg_kb_admin)
    elif update.message.text == "Остановить":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=markup_stg_kb_admin)
    elif update.message.text == "Таймер":
        update.message.reply_text("Управление таймером", reply_markup=markup_timer_kb_admin)
    elif update.message.text == "Включить таймер (2 мин)":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=markup_snt_kb_admin)
    elif update.message.text == "Статусы":
        update.message.reply_text("Управление статусами", reply_markup=markup_statuses_kb_admin)
    elif update.message.text == "Остаток времени":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=markup_hmt_kb_admin)
    elif update.message.text == "Лог поведения":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=markup_l_kb_admin)
    elif update.message.text == "Кол-во рыб в пруду":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=markup_hmfip_kb_admin)
    elif update.message.text == "Кол-во рыб в N раунде":
        update.message.reply_text("Нажмите на команду для выполнения действия", reply_markup=markup_hmfir_kb_admin)
    elif update.message.text == "Назад <-":
        update.message.reply_text("вас перенесло в главное меню", reply_markup=markup_main_kb_admin)


def start(update, context):
    if check_Admin(update.message.chat.id):
        update.message.reply_text("""Привет! Начнём игру!""", reply_markup=markup_main_kb_admin)
    else:
        update.message.reply_text("""Привет! Начнём игру!""", reply_markup=markup_main_kb_user)


def register(update, context):
    update.message.reply_text("""Напишите имя пользователя, под которым вы хотите войти.
    Если вы хотите прервать диалог напишите Стоп.""")
    return 1


def register1(update, context):
    if update.message.text.lower() == "стоп":
        update.message.reply_text("Вы прервали диалог")
        return ConversationHandler.END
    return_check_name = check_name(update.message.text, update.message.chat.id)
    if return_check_name == 1:
        update.message.reply_text("""Вы заходите под именем Администратра, напишите пароль.
    Если вы хотите прервать диалог напишите Стоп.""")
        context.user_data['return_check_name'] = return_check_name
        return 2
    elif return_check_name == 2:
        update.message.reply_text("""Имя пользователя уже занято, введите другое.
    Если вы хотите прервать диалог напишите Стоп.""")
    elif return_check_name == 3:
        update.message.reply_text("""Вы уже зарегистрированы""")
    elif return_check_name == 0:
        context.user_data['return_check_name'] = return_check_name
        context.user_data["name"] = update.message.text
        update.message.reply_text("""Введитете код, который позволит вам присоединиться к игре.
    Если вы хотите прервать диалог напишите Стоп.""")
        return 2


def register2(update, context):
    if update.message.text.lower() == "стоп":
        update.message.reply_text("Вы прервали диалог")
        return ConversationHandler.END
    return_check_name = context.user_data['return_check_name']
    if return_check_name == 1:
        if check_password(update.message.text):
            change_Admin(update.message.chat.id)
            update.message.reply_text("Вы получили права Администратора", reply_markup=markup_main_kb_admin)
            return ConversationHandler.END

    elif return_check_name == 0:
        if check_register():
            if check_game_code(update.message.text):
                add_user(context.user_data["name"], update.message.text, int(update.message.chat.id))
                change_game_code(update.message.text, context.user_data["name"])
                update.message.reply_text("Вы успешно зашли под именем {}".format(context.user_data["name"]),
                                          reply_markup=markup_main_kb_user)
                return ConversationHandler.END
            else:
                update.message.reply_text("""Вы ввели неправильный код, попробуйте еще раз.
    Если вы хотите прервать диалог напишите Стоп.""")
        else:
            update.message.reply_text("В данный момент регистрация закрыта")
            return ConversationHandler.END


def start_game(update, context):
    if check_Admin(update.message.chat.id):
        update.message.reply_text("""Введите код, который позволит пользователям присоединиться к игре.
    Если вы хотите прервать диалог напишите Стоп.""")
        return 1
    else:
        update.message.reply_text("Только Администратор может пользоваться данной командой")
        return ConversationHandler.END


def start_game1(update, context):
    if update.message.text.lower() == "стоп":
        update.message.reply_text("Вы прервали диалог")
        return ConversationHandler.END
    if check_Admin(update.message.chat.id):
        change_game_code(update.message.text, "Admin")
        open_register()
        update.message.reply_text("Вы открыли регистрацию, код: {}".format(update.message.text))
        context.bot.send_message(update.message.chat.id, 'Чтобы закрыть регистрацию и начать игру нажмите /game')
        return ConversationHandler.END
    else:
        update.message.reply_text("Только Администратор может пользоваться данной командой")
        return ConversationHandler.END


def first_round(update, context):
    global user_table_list
    if check_Admin(update.message.chat.id):
        close_register()
        ids = get_ids_playing()
        user_table_list = create_table("game_table.xlsx")
        fishes = get_fishes()
        fish_flag_open()
        create_log_file()
        add_line("1 Раунд")
        for id in ids:
            context.bot.send_message(id, text=f'Начался первый раунд! в пруду {fishes} рыб')

    else:
        update.message.reply_text("Только Администратор может пользоваться данной командой")
        return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Вы остановили диалог")
    pass


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
    fish_in_rounds_handler = ConversationHandler(
        entry_points=[CommandHandler('how_much_fish_in_round', how_much_fish_in_round)],
        states={
            1: [MessageHandler(Filters.text, how_much_fish_in_round1, pass_user_data=True)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    register_handler = ConversationHandler(
        entry_points=[CommandHandler('register', register)],
        states={
            1: [MessageHandler(Filters.text, register1, pass_user_data=True)],
            2: [MessageHandler(Filters.text, register2, pass_user_data=True)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    start_game_handler = ConversationHandler(
        entry_points=[CommandHandler('start_game', start_game)],
        states={
            1: [MessageHandler(Filters.text, start_game1)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    fishing_handler = ConversationHandler(
        entry_points=[CommandHandler('fishing', fishing)],
        states={
            1: [MessageHandler(Filters.text, fishing1)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    hand = CommandHandler('game', first_round)
    fake_hand = CommandHandler('fake_task', fake_task)
    dp.add_handler(fish_in_rounds_handler)
    dp.add_handler(fake_hand)
    dp.add_handler(hand)
    dp.add_handler(fishing_handler)
    dp.add_handler(register_handler)
    dp.add_handler(start_game_handler)
    dp.add_handler(CommandHandler("how_much_fish_in_pond", how_much_fish_in_pond))
    dp.add_handler(CommandHandler("stop_game", stop_game))
    dp.add_handler(CommandHandler("rounds", rounds))
    # Регистрируем обработчик в диспетчере.
    text_handler = MessageHandler(Filters.text, send_message)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("my_fish", my_fish))
    dp.add_handler(CommandHandler("log_conduct", log_conduct))
    dp.add_handler(text_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
