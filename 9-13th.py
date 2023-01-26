import datetime
from functools import wraps

a = datetime.datetime.now()
s = a.year

class Repeater:
    """декоратор"""
    def __init__(self, n):
        self.n = n
    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print("<strong>")
            f(*args, **kwargs)
            print("</strong>")
        return wrapper

class person():
    """Информация о человеке"""

    def __init__(self, surname, name, bday):
        self.surname = surname
        self.name = name
        self.bday = bday

    @Repeater(3)
    def inf(self):
        """Вывод информации"""
        print("Фамилия: " + self.surname + "Имя: " + self.name + "Год рождения " + str(self.bday))

    def age_of_person(self):
        print("Возраст человека: " + str(s - self.bday))  # подсчет возраста человека


class pers(person):
    """Подкласс person"""

    def __init__(self, surname, name, bday):
        super().__init__(surname, name, bday)

    def age_of_person(self):
        """Подсчет в днях"""
        print("Возраст человека: " + str(s - self.bday))  # как сделать вывод в днях вопрос


person3 = pers("Александрович", "Юрий", 2000)
person1 = pers("Михальков ", "Виталий ", 1985)
person2 = person("Юрьевич ", "Александр ", 1964)

person1.inf()  # вывод инф-ции о человеке
person1.age_of_person()
person2.inf()
person2.age_of_person()




