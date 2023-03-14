words = ''
while True:
    word = input('Введите слово: ')
    if word == 'stop':
        break
    else:
        words = words + word + ' '
print(words)