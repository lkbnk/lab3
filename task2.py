print('Начинаем игру, для выхода из программы введите стоп')
while True:
    word = str(input('Введите слово: '))
    if word == 'стоп':
        break
    elif word == '':
        print('Вы ввели ни одного символа')
    elif 'ф' in word:
        print('Это редкое слово')
    else:
        print('Это не очень редкое слово')