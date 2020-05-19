from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from token_t_bot import TOKEN
from register_func import check_name, check_password, register_flag, add_user, change_game_code, \
    check_Admin, change_Admin, check_register, close_register, open_register, check_game_code, get_ids_playing
from telegram import ReplyKeyboardMarkup


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
r_kb_user = [["/registration", "Назад"]]
f_kb_user = [['1', "2", "3"], ['Назад']]

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


def how_much_fish_in_pond():
    pass


def how_much_time():
    pass


def my_fish():
    pass


def fishing():
    pass


def stop_game():
    pass


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


def log_conduct():
    pass


def how_much_fish_in_round():
    pass


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
    return_check_name = check_name(update.message.text)
    if return_check_name == 1:
        update.message.reply_text("""Вы заходите под именем Администратра, напишите пароль.
    Если вы хотите прервать диалог напишите Стоп.""")
        context.user_data['return_check_name'] = return_check_name
        return 2
    elif return_check_name == 2:
        update.message.reply_text("""Имя пользователя уже занято, введите другое.
    Если вы хотите прервать диалог напишите Стоп.""")
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
            update.message.reply_text("Вы получили права Администратора")
            return ConversationHandler.END

    elif return_check_name == 0:
        if check_register():
            if check_game_code(update.message.text):
                add_user(context.user_data["name"], update.message.text, int(update.message.chat.id))
                change_game_code(update.message.text, context.user_data["name"])
                update.message.reply_text("Вы успешно зашли под именем {}".format(context.user_data["name"]))
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
        return ConversationHandler.END
    else:
        update.message.reply_text("Только Администратор может пользоваться данной командой")
        return ConversationHandler.END


def first_round(update, context):
    if check_Admin(update.message.chat.id):
        close_register()
        ids = get_ids_playing()
        for id in ids:
            context.bot.send_message(id, text='Начался первый раунд!')

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
    start_game_handler = ConversationHandler(
        entry_points=[CommandHandler('register', register)],
        states={
            1: [MessageHandler(Filters.text, register1, pass_user_data=True)],
            2: [MessageHandler(Filters.text, register2, pass_user_data=True)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    register_handler = ConversationHandler(
        entry_points=[CommandHandler('start_game', start_game)],
        states={
            1: [MessageHandler(Filters.text, start_game1)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    hand = CommandHandler('first_round', first_round)
    dp.add_handler(hand)
    dp.add_handler(register_handler)
    dp.add_handler(start_game_handler)

    # Регистрируем обработчик в диспетчере.
    text_handler = MessageHandler(Filters.text, send_message)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(text_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
