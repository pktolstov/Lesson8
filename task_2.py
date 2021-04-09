"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class My_Class_Exception(Exception):

    def __str__(self):
        return f'Деление на 0 невозможно, введите корректно делитель>>>'


class Devision:

    def __init__(self, number_one: int, number_two: int):
        self.number_one = number_one
        self.number_two = number_two

    def __str__(self):
        return f'{self.number_one} / {self.number_two} '

    def try_dev(self):
        try:
            
            if self.number_two == 0:
                raise My_Class_Exception

            else:
                print(self.number_one / self.number_two)
        except My_Class_Exception as exception:
            print(exception)


a = Devision(1, 0)
print(a)
a.try_dev()

b = Devision(5, 3)
b.try_dev()

