"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex_number:
    def __init__(self, deystv_part, mnim_part):
        self.deystv_part = deystv_part
        self.mnim_part = mnim_part

    def __str__(self):
        return f'{self.deystv_part}+ {self.mnim_part}i'

    def __add__(self, other):
        return f'Сумма действительных чисел: {self.deystv_part}+({self.mnim_part}i) + {other.deystv_part}+({other.mnim_part}i) = {self.deystv_part + other.deystv_part} + {self.mnim_part + other.mnim_part}i'

    def __mul__(self, other):
        return f'Произведение действительных чисел: {self.deystv_part}+({self.mnim_part}i) * {other.deystv_part}+({other.mnim_part}i) = {self.deystv_part * other.deystv_part - self.mnim_part * other.mnim_part} + {self.deystv_part * other.mnim_part + self.mnim_part * other.deystv_part}i'


first_number = Complex_number(9, -11)
second_number = Complex_number(11, 13)

print(first_number + second_number)
print(first_number * second_number)
