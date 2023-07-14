'''
Задание № 7
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
    !!! В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''

import sys
from datetime import datetime

MinDate = 1
MaxYear = 9999
MaxMonth = 12
MaxDay = 31

def is_real_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))

    if not(MinDate <= year <= MaxYear and MinDate <= month <= MaxMonth and MinDate <= day <= MaxDay):
        return False

    if not(month in (4, 6, 9, 11) and day <= 30):
        return False

    if not(month == 2 and _is_leap_year(year) and day == 29):
        return False

    if not(month == 2 and not _is_leap_year(year) and day == 28):
        return False
    
    return True

def _is_leap_year(year: int) -> bool:
    return year % 4 == 0 or year % 100 == 0 and year % 400 != 0

def is_valid_date(date_str):
    try:
        value = datetime.strptime(date_str, "%d.%m.%Y").date()
        day, month, year = map(int, date_str.split('.'))
        if _is_leap_year(year) == 1:
            return True
        return True
    except:
        return False

if __name__ == '__main__':
    date_str = input('Введите дату в формате DD.MM.YYYY: ')
    print(is_valid_date(date_str))
    