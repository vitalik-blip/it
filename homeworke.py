#begin = int(input('Введите начало отрезка: '))
#finish = int(input("Введите конец отрезка: "))
#step = int(input('Введите шаг: '))
#for x in range(finish, begin, step):
#    y = (x ** 3) + 2 * (x ** 2) - (4 * x) + 1
#    print('В точке', x, 'функция равна', y)
#if begin > finish :
#    begin, finish = finish, begin
#if step > 0:
 #       step = step * -1
#N = int(input('Введите число: '))
#s = 0
#print('При N =', N, 'элементы выражения будут равны:')
#for n in range(0, N):
#    print('n =', n)
#    elem = (-1) ** n * 1 / (2 ** n)
#    print('elem =', '(-1)**',n, '* 1/(2**', n,'),=', elem)
 #   s += (-1) ** n * 1 / (2 ** n)
#print('сумма равна: ', s)
boys = int(input('Введите кол-во мальчиков: '))
girls = int(input('Введите кол-во девочек: '))
result = ''
if boys > 2 * girls or girls > 2 * boys:
  result += 'Нет решения'
elif boys > girls:
  extra = boys - girls
  for bg in range(girls - extra):
    result += 'BG'
  for bgb in range(extra):
    result += 'BGB'
else:
  extra = girls - boys
  for gb in range(boys - extra):
    result += 'GB'
  for gbg in range(extra):
    result += 'GBG'
print('Ответ:', result)