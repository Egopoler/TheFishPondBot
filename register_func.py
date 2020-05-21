import db_session
from users import User

register_flag = False


def check_name(name, user_id_, db="TheFishPondBot.sqlite"):
    """
    Функция проверяет на уникальность имя пользователя(name) в таблице
    :param name: Имя пользователя
    :param db: База данных
    :return: ответ для проверки
    """
    db_session.global_init(db)
    session = db_session.create_session()
    for user in session.query(User).filter(User.name == name):
        if user.id == 1:
            return 1  # вход под именем администратора
        return 2  # имя не уникально
    for user in session.query(User).filter(User.user_id == user_id_):
        return 3  # игрок уже зарегистрирован
    return 0  # имя уникально


def check_password(password, name="Admin", db="TheFishPondBot.sqlite"):
    """
    Проверяет пароль
    :param password: пароль, который ввел пользователь
    :param name: имя пользователя
    :param db: таблица
    :return: True/False
    """
    db_session.global_init(db)
    session = db_session.create_session()
    for user in session.query(User).filter(User.name == name):
        if user.password == password:
            return True
    return False


def check_register():
    """
    Функция проверяет закрыта/открыта регистрация
    :return: True/False
    """
    global register_flag
    return register_flag


def close_register():
    """
    Закрывает регистрацию
    :return: None
    """
    global register_flag
    register_flag = False


def open_register():
    """
    Открывает регистрацию
    :return: None
    """
    global register_flag
    register_flag = True


def change_Admin(admin_id, db="TheFishPondBot.sqlite"):
    """Сменяет user_id Admin"""
    db_session.global_init(db)
    session = db_session.create_session()
    user = session.query(User).filter(User.name == "Admin").first()
    user.user_id = admin_id
    session.commit()


def check_Admin(user_id, db="TheFishPondBot.sqlite"):
    """Проверяет, является ли пользователь Admin"""
    db_session.global_init(db)
    session = db_session.create_session()
    for user in session.query(User).filter(User.name == "Admin"):
        if int(user_id) == user.user_id:
            return True
    return False


def check_game_code(code, db="TheFishPondBot.sqlite", admin="Admin"):
    """Проверка игрового кода для входа"""
    db_session.global_init(db)
    session = db_session.create_session()
    for user in session.query(User).filter(User.name == admin):
        if str(user.game) == str(code):
            return True
    return False


def change_game_code(code, user_name, db="TheFishPondBot.sqlite"):
    """Изменение игрового кода для входа"""
    db_session.global_init(db)
    session = db_session.create_session()
    user = session.query(User).filter(User.name == user_name).first()
    user.game = str(code)
    session.commit()


def add_user(name, game, user_id_, db="TheFishPondBot.sqlite"):
    """Добавляет пользователя"""
    db_session.global_init(db)
    session = db_session.create_session()
    user = User()
    user.name = name
    user.game = game
    user.user_id = user_id_
    user.fish = 1  # Кол-во рыбы по умолчанию
    session.add(user)
    session.commit()


def get_name_playing(db="TheFishPondBot.sqlite"):
    db_session.global_init(db)
    session = db_session.create_session()
    game_admin = session.query(User.game).filter(User.name == 'Admin').first()[0]
    lst_of_names = []
    for user in session.query(User).filter(User.game == game_admin):
        if user.name not in lst_of_names:
            if user.name != 'Admin':
                lst_of_names.append(user.name)
    return lst_of_names


def get_ids_playing(db="TheFishPondBot.sqlite"):
    db_session.global_init(db)
    session = db_session.create_session()
    game_admin = session.query(User.game).filter(User.name == 'Admin').first()[0]
    lst_of_ids = []
    for user in session.query(User).filter(User.game == game_admin):
        if user.user_id not in lst_of_ids:
            lst_of_ids.append(user.user_id)
    return lst_of_ids


def get_name_for_id(user_id_, db="TheFishPondBot.sqlite"):
    db_session.global_init(db)
    session = db_session.create_session()
    name = session.query(User.name).filter(User.user_id == user_id_).first()[0]
    return name


def get_id_for_name(user_name_, db="TheFishPondBot.sqlite"):
    db_session.global_init(db)
    session = db_session.create_session()
    id = session.query(User.user_id).filter(User.user_name_ == user_name_).first()[0]
    return id


def clear_game(db="TheFishPondBot.sqlite"):
    db_session.global_init(db)
    session = db_session.create_session()
    for user in session.query(User).filter(User.name != "Admin"):
        session.delete(user)
    admin = session.query(User).filter(User.name == "Admin").first()
    admin.game = None
    session.commit()
