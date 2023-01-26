import datetime

d1 = datetime.datetime.strptime(input("Введите дату(dd/mm/yyyy H:M): \n"), "%d/%m/%Y %H:%M")
d2 = datetime.datetime.strptime(input("Введите дату(dd/mm/yyyy H:M): \n"), "%d/%m/%Y %H:%M")

timedelta = d1 - d2

print(timedelta)