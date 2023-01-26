import datetime

g1 = datetime.datetime.strptime(input("Введите первую дату(dd/mm/yyyy H:M): \n"), "%d/%m/%Y %H:%M")
g2 = datetime.datetime.strptime(input("Введите вторую дату(dd/mm/yyyy H:M): \n"), "%d/%m/%Y %H:%M")
g3 = datetime.datetime.strptime(input("Введите третью дату(dd/mm/yyyy H:M): \n"), "%d/%m/%Y %H:%M")

if g1 > g3 > g2:
    print("Лежит между")
else:
    print("Не лежит")
