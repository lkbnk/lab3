import random

error = 0
correct = 0

while error < 3:
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    result = a + b
    answer = input('Сколько будет ' + str(a) + ' + ' + str(b) + ': ')

    if int(answer) == result:
        print('Правильно!')
        correct += 1
    else:
        print('Ответ неверный')
        error += 1

print('Количество правильных ответов: ' + str(correct))
