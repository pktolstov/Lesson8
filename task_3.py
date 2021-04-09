"""
3. Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class MyException(Exception):
    def __str__(self):
        return f'Вы ввели не число!'


class CreateList:
    user_list = []

    # def __init__(self):
    # self.user_list=user_list
    def __str__(self):
        return f'Список: {self.user_list}'

    def check_list(self):
        count = 'str'
        while count != 'stop':
            el = input('Введите элемент списка или введите stop для выхода>> ')
            if el.lower()=='stop':

                count = 'stop'
                print(f'Текущий список: {self.user_list}')
                break

            try:

                if not el.isdigit() and el != 'stop':
                    raise MyException

                else:
                    self.user_list.append(int(el))
                    #print(self.user_list)
            except MyException as my_except:

                print(my_except)
                continue


a = CreateList()
a.check_list()
