import random
right_ans = int(input('Введите число от 1 до 100: '))
num1 = 1
num2 = 101
right = False
tries = 1
while not right:
 comp_answer = random.randint(num1, num2)
 if comp_answer > right_ans:
   num2 = comp_answer
 elif comp_answer < right_ans:
   num1 = comp_answer + 1
 else:
   print(f'комп угадал за {tries} попыток')
   right = True
 tries += 1