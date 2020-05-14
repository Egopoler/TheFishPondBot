import db_session
from users import User

register_flag = False
Admin = ""


def check_name(name, db="TheFishPondBot.sqlite"):
    db_session.global_init(db)
    session = db_session.create_session()
    for user in session.query(User).filter(User.name == name):
        if user.id == 1:
            return 1  # вход под именем администратора
        return 2  # имя не уникально
    return 0  # имя уникально


def check_password(password, name="Admin", db="TheFishPondBot.sqlite"):
    db_session.global_init(db)
    session = db_session.create_session()
    for user in session.query(User).filter(User.name == name):
        if user.password == password:
            return True
    return False


def check_register():
    global register_flag
    return register_flag


def close_register():
    global register_flag
    register_flag = False


def open_register():
    global register_flag
    register_flag = True


def change_Admin(admin_id, db="TheFishPondBot.sqlite"):
    db_session.global_init(db)
    session = db_session.create_session()
    user = session.query(User).filter(User.name == "Admin").first()
    user.user_id = admin_id


def check_Admin(user_id, db="TheFishPondBot.sqlite"):
    db_session.global_init(db)
    session = db_session.create_session()
    for user in session.query(User).filter(User.name == "Admin"):
        if int(user_id) == user.user_id:
            return True
    return False


def check_game_code(code, db="TheFishPondBot.sqlite", admin="Admin"):
    db_session.global_init(db)
    session = db_session.create_session()
    for user in session.query(User).filter(User.name == admin):
        if user.game == code:
            return True
    return False


def add_user(name, game, user_id_, db="TheFishPondBot.sqlite"):
    user = User()
    user.name = name
    user.game = game
    user.user_id = user_id_
    db_session.global_init(db)
    session = db_session.create_session()
    session.add(user)
    session.commit()