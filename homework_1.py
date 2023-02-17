# Практическое задание 1

print('Напишите программу, удаляющую из текста все слова, содержащие ""абв"".')


def readfile(filename):
    with open(filename, 'r') as f:
        content = f.read()
        f.close()
        return content


def write_to_file(filename, content):
    with open(filename, 'w+') as f:
        f.write(content)
        f.close()


text = readfile('homework_1/init_1.txt')
filtered_text = ' '.join(filter(lambda b, a='абв': a not in b, text.split(' ')))
write_to_file('homework_1/result_1.txt', filtered_text)
print(f'\nИсходный текст: \n{text}\n\n\nРезультат: \n{filtered_text}')
