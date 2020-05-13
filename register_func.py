import db_session
from users import User


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