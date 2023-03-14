from random import randint

error = 0
correct = 0

while error < 3:
    a = randint(0, 1000)
    b = randint(0, 1000)
    result = a + b
    answer = input('Сколько будет ' + str(a) + ' + ' + str(b) + ': ')

    if int(answer) == result:
        print('Правильно!')
        correct += 1
    else:
        print('Ответ неверный')
        error += 1

print('Количество правильных ответов: ' + str(correct))
