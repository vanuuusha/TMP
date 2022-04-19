from constants import ADMINPASSWORD, MAXEXPERIENCE, MAXLENNAME


def check_correct_admin_password(pas):
    if pas == ADMINPASSWORD:
        return True
    return False


def no_digit(text):
    for i in text:
        if i.isdigit():
            return False
    return True


def fio_checker(text):
    if len(text) > 1 and len(text) < MAXLENNAME:
        flag1 = True
    else:
        flag1 = False
    flag2 = no_digit(text)
    return text, flag1 and flag2


def experience_checker(text:str):
    for i in text:
        if not i.isdigit():
            return text, False
    if int(text) < 0 or int(text) > MAXEXPERIENCE:
        return text, False
    return int(text), True



