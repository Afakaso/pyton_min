mas = list(range(101, 1001))
i = 0
for n in mas:
    if(n % 2) == 0:
        i += n
print("Сумма четных чисел в массиве:", i)

i = 0
for n in mas:
    if(n % 2) == 1:
        i += n

print("Сумма нечетных чисел в массиве:", i)

