# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from token_t_bot import TOKEN
from register_func import check_name, check_password, register_flag, add_user, change_game_code, \
    check_Admin, change_Admin, check_register, close_register, open_register, check_game_code


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    mes = "Я получил сообщение " + update.message.text
    update.message.reply_text(mes)


def us_id(update, context):
    print(update)
    Admin = update.message.chat.id
    print(Admin)


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
    dp.add_handler(register_handler)
    dp.add_handler(start_game_handler)
    text_handler = MessageHandler(Filters.text, echo)

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(CommandHandler('us_id', us_id))
    dp.add_handler(text_handler)
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
