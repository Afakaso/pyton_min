import datetime

d1 = datetime.datetime.strptime(input("Введите дату(dd/mm/yyyy H:M): \n"), "%d/%m/%Y %H:%M")

print(str(d1.replace(hour=10)).rsplit(':', 1)[0])