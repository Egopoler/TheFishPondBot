# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from token_t_bot import TOKEN
from register_func import check_name, check_password, register_flag, add_user, \
    Admin, check_Admin, change_Admin, check_register, close_register, open_register, check_game_code


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
    global Admin
    Admin = update.chat.id
    print(Admin)


def register(update, context):
    update.message.reply_text("Напишите имя пользователя, под которым вы хотите войти")
    return 1


def register1(update, context):
    return_check_name = check_name(update.message.text)
    if return_check_name == 1:
        update.message.reply_text("Вы заходите под именем Администратра, напишите пароль")
        context.user_data['return_check_name'] = return_check_name
        return 2
    elif return_check_name == 2:
        update.message.reply_text("Имя пользователя уже занято, введите другое")
    elif return_check_name == 0:
        context.user_data['return_check_name'] = return_check_name
        context.user_data["name"] = update.message.text
        update.message.reply_text("Введитете код, который позволит вам присоединиться к игре")
        return 2


def register2(update, context):
    global Admin
    return_check_name = context.user_data['return_check_name']
    if return_check_name == 1:
        if check_password(update.message.text):
            change_Admin(update.chat.id)
            print(Admin)
    if return_check_name == 0:
        if check_register():
            if check_game_code(update.message.text):
                add_user(context.user_data["name"], update.message.text, int(update.chat.id))
                update.message.reply_text("Вы успешно зашли под именем {}".format(context.user_data["name"]))


def stop():
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
    register_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('register', register)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(Filters.text, register1, pass_user_data=True)],
            # Функция читает ответ на второй вопрос и завершает диалог.
            2: [MessageHandler(Filters.text, register2, pass_user_data=True)]
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(register_handler)

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
