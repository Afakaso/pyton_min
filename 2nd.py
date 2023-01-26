import datetime
import calendar

d = datetime.date(*map(int, input("Введите дату (dd/mm/yyyy)").split("/")[::-1]))
d1 = d.replace(day=1)
year = d.year
month = d.month
days = calendar.monthrange(year, month)[1]
d2 = d.replace(day=days)

print(d1.strftime("%a"))
print(d2.strftime("%a"))
print(d.strftime("%b"))
