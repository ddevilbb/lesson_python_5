# Практическое задание 4

print('Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.')


def encode_string(string):
    char, cnt = string[0], 0
    result = ''
    for i in string:
        if char != i:
            result += str(cnt) + char
            char, cnt = i, 1
        else:
            cnt += 1
    result += str(cnt) + char
    return result


def decode_string(string):
    result = ''
    cnt = 0
    for i in range(len(string)):
        char = string[i]
        if char.isdigit():
            cnt = int(char)
        else:
            result += char * cnt
            cnt = 0
    return result


input_string = input('Введите текст для кодировки: ')
encoded_string = encode_string(input_string)
print(f'Результат кодирования: {encoded_string}')
print(f'Результат декодирования: {decode_string(encoded_string)}')
