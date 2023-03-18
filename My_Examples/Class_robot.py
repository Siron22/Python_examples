class Robot:
    """   Представляет робота с именем.    """
    population = 0  # Переменная класса, содержащая количество роботов

    def __init__(self, name):
        '''Инициализация данных.'''
        self.name = name
        print(f'(Инициализация {self.name})')
        Robot.population += 1  # При создании этой личности, робот добавляется к переменной 'population'

    def __del__(self):
        '''Я умираю.'''
        print('{0} уничтожается!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population))

    def sayHi(self):
        '''Приветствие робота. Да, они это могут.'''
        print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))

    def howMany():
        '''Выводит численность роботов.'''
        print('У нас {0:d} роботов.'.format(Robot.population))

    howMany = staticmethod(howMany)


droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()
print("\nЗдесь роботы могут проделать какую-то работу.\n")
print("Роботы закончили свою работу. Давайте уничтожим их.")
# del droid1
# del droid2
# Robot.howMany()
