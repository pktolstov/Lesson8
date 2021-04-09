"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.
"""


class Error_store(Exception):


    def __str__(self):
        return f'{self}'
class Error_add_tech(Error_store):
    def __str__(self):
        return f'Ошибка добаления на склад! Проверьте доступный объем хранилища'
class Error_transfer(Error_store):
    def __str__(self):
        return f'Ошибка списания товара! Проверьте доступное количество техники'







class Store:
    departments=['managers', 'marketing', 'accaunting']
    stock = {'printers': 0, 'scaners': 0, 'mfu': 0}
    max_stock=10
    count=0

    def __init__(self, count):
        self.count = count



    @classmethod
    def incoming_unit(self, type, amount: int):
        try:
            if Store.count+ amount <=Store.max_stock:
                if Store.stock[type] >= 0 :
                    Store.stock[type] = Store.stock[type] + amount
                    Store.count+=amount

                else:
                    Store.stock[key] = amount
                    return Store.stock
            else:
                raise Error_add_tech
        except Error_add_tech as adderr:
            print(adderr)





    @classmethod
    def outgoing_unit(self, type, amount: int):

        if Store.stock[type] - amount >= 0:
            Store.stock[type] - amount

        else:
            print(f'Недостаточно товара на складе {type}, {abs(Store.stock[type] - amount)}')

        return Store.stock[type]


class Periphery:
    def __init__(self, adf='no', duplex='no', format='A4', network='no'):
        self.adf = adf
        self.duplex = duplex
        self.format = format
        self.network = network


class Printers(Periphery):
    type = 'printers'

    def __init__(self, model, speed_print, *args, **kwargs):
        self.model = model
        self.speed_print = speed_print

        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'принтер {self.__dict__}'


class Scaners(Periphery):
    type = 'scaners'

    def __init__(self, model, scan_speed, *args, **kwargs):
        self.model = model
        self.scan_speed = scan_speed

        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'Сканер {self.model}'


class Multi_func_machine(Periphery):
    type = 'mfu'

    def __init__(self, model, copy_speed, *args, **kwargs):
        self.model = model
        self.copy_speed = copy_speed

        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'МФУ {self.model}'


hp = Printers(model='HP P1005', speed_print=35)
print(hp)

canon_scan = Scaners(model='Canon Lide120', scan_speed=20)
print(canon_scan)

kyocera = Multi_func_machine(model='Kyocera M2040', copy_speed=40)
print(kyocera)
Store.incoming_unit(hp.type, 7)
Store.outgoing_unit(canon_scan.type, 2)
Store.outgoing_unit(kyocera.type, 1)

print(Store.stock)
Store.incoming_unit(canon_scan.type, 3)
Store.incoming_unit(kyocera.type, 1)
print(Store.stock)
