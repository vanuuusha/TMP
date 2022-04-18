import datetime


def no_digit(text):
    for i in text:
        if i.isdigit():
            return False
    return True


def fio_checker(text):
    if len(text) > 1 and len(text) < 20:
        flag1 = True
    else:
        flag1 = False
    flag2 = no_digit(text)
    return text, flag1 and flag2


def age_checker(text, stoper):
    try:
        date = datetime.datetime.strptime(text, '%d.%m.%Y')
        now_time = datetime.datetime.now()
    except ValueError:
        return False
    if stoper == 0:
        flag = date > now_time
    else:
        start_year = date.year
        for year in range(start_year, now_time.year):
            if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
                stoper += 1
        flag = (now_time - date).days < stoper
    if (2022 - int(date.year)) > 100 or flag:
        return False
    return True


