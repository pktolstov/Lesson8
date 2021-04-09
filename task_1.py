"""
1. Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, user_date: str):
        self.user_date = user_date
    def __str__(self):
        return f'{self.user_date}'

    @classmethod
    def str_to_digit(cls, user_date):
        int_date = tuple(int(i) for i in (user_date.split('-')))
        return int_date         #f'{int_date[0]}-{int_date[1]}-{int_date[2]}'

    @staticmethod
    def valid_date(source_date):
        s_date = Date.str_to_digit(source_date)
        val_dict={31:[1,3,5,7,8,10,12], 30:[2,4,6,9,11], 28:2}
        if s_date[1] in val_dict[31] and 1 <= s_date[0] <= 31 and 1900 <= s_date[2] <= 2021:
            return f'Date {source_date} is correct!'
        elif s_date[1] in val_dict[30] and 1 <= s_date[0] <= 30 and 1900 <= s_date[2] <= 2021:
            return f'Date {source_date} is correct!'
        elif s_date[1] == val_dict[28] and 1 <= s_date[0] <= 28 and 1900 <= s_date[2] <= 2021:
            return f'Date {source_date} is correct!'
        else:
            return f'Date {source_date} is INCORRECT!'


d = Date('1-13-2021')
print(d)
print(d.user_date)
print(d.str_to_digit('1-12-2021'))
print(Date.str_to_digit('29-01-2021'))
print(Date.valid_date('12-07-2020'))
print(Date.valid_date('1-13-1700'))
print(Date.valid_date('28-02-2020'))
print(Date.valid_date('31-04-2021'))
