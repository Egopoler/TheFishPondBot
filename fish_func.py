import db_session
from users import User
from random import choice
from log_in_game import add_line

fish_flag = False


def breeding(number_of_fish):
    number_of_fish += number_of_fish // 2
    return number_of_fish


def del_fish(name, fish=1, db="TheFishPondBot.sqlite"):
    db_session.global_init(db)
    session = db_session.create_session()
    user = session.query(User).filter(User.name == name).first()
    user.fish = user.fish - fish
    session.commit()


def check_life(name, db="TheFishPondBot.sqlite"):
    db_session.global_init(db)
    session = db_session.create_session()
    user = session.query(User).filter(User.name == name).first()
    if user.fish < 0:
        return False
    return True


def check_fish(name, db="TheFishPondBot.sqlite"):
    db_session.global_init(db)
    session = db_session.create_session()
    user = session.query(User).filter(User.name == name).first()
    return user.fish


def get_fish(name, fish, db="TheFishPondBot.sqlite"):
    db_session.global_init(db)
    session = db_session.create_session()
    user = session.query(User).filter(User.name == name).first()
    user.fish = user.fish + fish
    session.commit()


def caught_all_in_round(data, db="TheFishPondBot.sqlite"):
    """
    функция считает общее кол-во пойманных рыб за раунд
    :param data: список с именами пользователей, которые участвуют в игре
    :param db:
    :return: сумма рыб
    """
    db_session.global_init(db)
    session = db_session.create_session()
    summ = 0
    for user in session.query(User).filter(User.name.in_(data)):
        summ += user.caught
    return summ


def caught_in_round(user_id_, caught_, db="TheFishPondBot.sqlite"):
    """
    функция записывает в бд кол-во пойманных рыб
    :param user_id_: айди пользователя
    :param caught_: скорлько рыб поймал в раунде
    :param db:
    :return:
    """
    db_session.global_init(db)
    session = db_session.create_session()
    user = session.query(User).filter(User.user_id == user_id_).first()
    user.caught = caught_
    session.commit()


def fish_flag_open():
    global fish_flag
    fish_flag = True


def fish_flag_close():
    global fish_flag
    fish_flag = False


def fish_flag_check():
    global fish_flag
    return fish_flag


def caught_check(id, db="TheFishPondBot.sqlite"):
    db_session.global_init(db)

    session = db_session.create_session()
    caught = session.query(User.caught).filter(User.user_id == id).first()[0]
    return caught


def get_caught_from_db(names_list, db="TheFishPondBot.sqlite"):
    list_return = []
    db_session.global_init(db)
    session = db_session.create_session()
    for name in names_list:
        caught = session.query(User.caught).filter(User.name == name).first()[0]
        code = session.query(User.game).filter(User.name == name).first()[0]
        if code is None:
            caught = '-'
        elif caught is None:
            caught = 0
            add_line("{} прогулял рыбалку и получил 0 рыб".format(name))
        list_return.append(caught)
    return list_return


def erease_caught(names_list, db="TheFishPondBot.sqlite"):
    db_session.global_init(db)
    session = db_session.create_session()
    for name in names_list:
        user = session.query(User).filter(User.name == name).first()
        user.caught = None
    session.commit()


def money():
    return choice(("Орёл", "Решка"))

