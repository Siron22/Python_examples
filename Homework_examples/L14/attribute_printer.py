"""
Написать класс-миксин, наследуя который объект будет выводится в консоль в виде имени класса и словаря аттрибутов со значениями.
class AttributePrinterMixin:
    pass

Протектед и приватные аттрибуты должны выводить только свое имя (без знака подчеркивания для протектед и префикса "_<имя класса>__")
Каждя строка с полем начинается с символа табуляции.
Если класс наслудует другие классы, их аттрибуты тоже должны выводится по тем же правилам.

Например:
class A(AttributePrinterMixin):

    def __init__(self):
        self.public_filed = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]

a = A()
print(a)
A: {
	public_filed: 3
	protected_field: q
	private_field: [1, 2, 3]
}
"""


class AttributePrinterMixin:

    def __str__(self):
        new_line = '\n'
        attributes_dict = self.__dict__
        res = []
        class_names = [class_.__name__ for class_ in self.__class__.__mro__]
        class_names.remove('object')
        class_names.remove('AttributePrinterMixin')

        private_prefixes = [f"_{class_name}__" for class_name in class_names]

        for attribute_full_name in attributes_dict:
            if list(filter(lambda prefix: attribute_full_name.startswith(prefix), private_prefixes)):
                attribute_updated_name = attribute_full_name[attribute_full_name.index('__') + 2:]
            elif attribute_full_name.startswith('_'):
                attribute_updated_name = attribute_full_name[1:]
            else:
                attribute_updated_name = attribute_full_name

            res.append(f"\t{attribute_updated_name}: {attributes_dict[attribute_full_name]}")

        print(res)

        return f"{self.__class__.__name__}: {{{new_line}" \
               f"{new_line.join(res)}" \
               f"{new_line}}}"


class Mega:
    def __init__(self):
        self.mega_public = 111
        self._mega_protected = 345
        self.__mega_private = 'mega'


class Super(Mega):
    def __init__(self):
        super().__init__()
        self.super_public_field = 444
        self._super_protected_field = 'ppp'
        self.__super_private_field = [1, 2, 3]
        self.__private_as_super = '__private_as_super'


class Super2:
    def __init__(self):
        super().__init__()
        self.super2_public_field = 222444
        self._super2_protected_field = '222ppp'
        self.__super2_private_field = [222, 1, 2, 3]


class A(Super, Super2, AttributePrinterMixin):

    def __init__(self):
        super().__init__()
        Super2.__init__(self)
        self.public_filed = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]
        self.__private_as_super = '__private_as_super'
        self.__private__dunder__score = '__private__dunder__score'

    @property
    def age(self):
        return 'age'


a = A()
print(a)
