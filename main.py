# class Ring:
#     a = 2
#     b = 'Color'
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#       def __del__(self):
#           print('Delete')
#
#       def get_info(self):
#           return self.x, self.y
#
# a = Ring(10, 22)
# print(a.__dict__)
# 
#
#  class Point:
#      def __new__(cls, *args, **kwargs):
#          print('Request for __new__' + str(cls))
#          return super().__new__(cls)
#
#      def __init__(self, x=0, y=0):
#          print('Request for __init__' + str(self))
#          self.x = x
#          self.y = y
#
#
#  pt = Point(1, 2)
#  print(pt)
#
#
#  class Vector:
#      MIN = 0
#      MAX = 100
#
#      @classmethod
#      def validate(cls, arg):   #Ссылка на класс Vector
#          return cls.MIN < arg < cls.MAX
#
#      def __init__(self, x, y):
#          self.x = self.y = 0
#          if self.validate(x) and self.validate(y):
#              self.x = x
#              self.y = y
#
#              print(self.norm2(self.x, self.y))
#
#      def get_record(self):
#          return self.x, self.y
#
#      @staticmethod         #Независимая функция Класса Vector
#      def norm2(x, y):
#          return x*x + y*y
#
#  v = Vector(1, 20)
#  print(Vector.validate(5))
#  print(Vector.norm2(5, 6))
#  res = Vector.get_record(v)
#  print(res)
#
#
#  Инкапсуляция
#
# from accessify import private, protected
#
#  class Point:
#
#      def __init__(self, x=0, y=0):
#          self.__x = self.__y = 0
#          if self.check_value(x) and self.check_value(y):
#              self.__x = x
#              self.__y = y
#      @private
#      @classmethod
#      def __check_value(cls, x):
#          return type(x) in (int, float)
#
#      def set_core(self, x, y):
#          if self.check_value(x) and self.check_value(y):
#              self.__x = x
#              self.__y = y
#          else:
#              raise ValueError('Координаты должны быть числами')
#
#      def get_core(self):
#          return self.__x, self.__y
#
#
#  pt = Point(1, 2)
#  pt.set_core(10, 20)
#  pt.check_value(5)
#
#
#   #__setattr__   __getattribute__   __getattr__   __delattr__
#
#  class Point:
#      MAX = 100
#      MIN = 0
#
#      def __init__(self, x, y):
#          self.x = x
#          self.y = y
#
#      def set_coord(self, x, y):
#          if self.MIN <= x <= self.MAX:
#              self.x = x
#              self.y = y
#       @classmethod
#       def set_bound(cls, left):
#           cls.MIN = left
#
#      def __getattribute__(self, item):
#          if item == "x":
#              raise ValueError('Доступ запрещен')
#          else:
#              print('__getattribute__')
#              return object.__getattribute__(self, item)
#
#      def __setattr__(self, key, value):
#          if key == 'z':
#              raise AttributeError('Недопуститмое имя атрибута')
#          else:
#              object.__setattr__(self, key, value)
#
#      def __getattr__(self, item):
#          return False
#
#      def __delattr__(self, item):
#          print('__del__' + item)
#          object.__delattr__(self, item)
#
#
#  pt1 = Point(1, 2)
#  pt2 = Point(10, 20)
#  pt1.yy = 10
#  del pt1.x
#  print(pt1.__dict__)
#
#
#   Паттерн Моносостояние
#
#  class ThreadData:
#      __shared_attrs = {
#          'name': 'thread1',
#          'data': {},
#          'id': 1
#      }
#
#      def __init__(self):
#          self.__dict__ = self.__shared_attrs
#
#
#    object Свойство Property
#
#
#  class Personal:
#      def __init__(self, name, old):
#          self.__name = name
#          self.__old = old
#      @property     Только перед геттером     Свойство получение инкапсл. атрибутов
#      def old(self):
#          return self.__old
#   Декораторы
#      @old.setter     Свойство изменения атрибута (Названия методов одинаково и отмечается .сеттер)
#      def old(self, old):
#          self.__old = old
#
#      @old.deleter
#      def old(self):
#          del self.__old
#
#  p = Personal('Sergey', 20)
#  del p.old
#  p.old = 45
#  print(p.__dict__)
#
#
#   Пример Property
#
# from string import ascii_letters
#
#
# class Person:
#     S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#     S_RUS_UPPER = S_RUS.upper()
#
#     def __init__(self, fio, old, ps, weight):
#         self.varify_fio(fio)
#         self.varify_old(old)
#         self.varify_ps(ps)
#         self.varify_weight(weight)
#
#         self.__fio = fio.split()
#         self.old = old
#         self.ps = ps
#         self.weight = weight
#
#     @classmethod
#     def varify_fio(cls, fio):
#         if type(fio) != str:
#             raise TypeError('Неверный тип данных')
#
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError('Неверный тип данных')
#
#         letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
#         for s in f:
#             if len(s) < 1:
#                 raise TypeError('В фио должен быть хотя бы один символ')
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В фио должны быть использованы только буквенные символы и дефис")
#
#     @classmethod
#     def varify_old(cls, old):
#         if type(old) != int or old < 14 or old > 120:
#             raise TypeError('Неверный возраст')
#
#     @classmethod
#     def varify_weight(cls, weight):
#         if type(weight) != float or weight < 20:
#             raise TypeError('Неправильный вес')
#
#     @classmethod
#     def varify_ps(cls, ps):
#         if type(ps) != str:
#             raise TypeError('Номер паспорта должен быть строкой')
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError('Неверный формат паспорта')
#
#         for i in s:
#             if not i.isdigit():
#                 raise TypeError('Серия номер паспорта должны быть числами')
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.varify_old(old)
#         self.__old = old
#
#     @property
#     def ps(self):
#         return self.__ps
#
#     @ps.setter
#     def ps(self, ps):
#         self.varify_ps(ps)
#         self.__ps = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.varify_weight(weight)
#         self.__weight = weight
#
#
# p = Person('Дементий Валерий Альбертович', 38, "1234 567890", 90.0)
# p.old = 100
# p.ps = "4567 123456"
# p.weight = 70.7
# print(p.old)
