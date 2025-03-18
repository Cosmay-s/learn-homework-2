"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    delta_one_day = timedelta(days=1)
    delta_thirty_days = timedelta(days=30)
    today = datetime.now()
    yesterday = today - delta_one_day
    tommorrow = today + delta_one_day
    thirty_days_ago = today - delta_thirty_days
    print(yesterday.strftime('%Y-%m-%d'))
    print(today.strftime('%Y-%m-%d'))
    print(tommorrow.strftime('%Y-%m-%d'))
    print(tommorrow.strftime('%Y-%m-%d'))
    print(thirty_days_ago.strftime('%Y-%m-%d'))


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_string = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date_string

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
