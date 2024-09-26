x = int(input('Введите сумму вклада: '))
p = int(input('Введите процент: '))
y = int(input('Введите сумму цели: '))
years = 0
while x < y:
    x *= 1 + p / 100
    x = int(100 * x) / 100
    years += 1
print(f'Понадобится {years} лет.')