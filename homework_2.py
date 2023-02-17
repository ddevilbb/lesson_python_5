# Практическое задание 2
from random import randint

min_turn_cnt = 1
max_turn_cnt = 28
player_names = []

print('Создайте программу для игры с конфетами человек против человека. \n'
      'Условие задачи: На столе лежит определённое количество конфет. Играют два игрока делая ход друг после друга. \n'
      'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. \n'
      'Все конфеты оппонента достаются сделавшему последний ход. \n'
      'Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?\n'
      '\na) Добавьте игру против бота\nb) Подумайте как наделить бота "интеллектом"')


def input_candies_amount():
    while True:
        try:
            cnt = int(input('Введите количество конфет: '))
            if cnt < 1:
                raise ValueError
            return cnt
        except ValueError:
            print('Допустимые значения: от 1 до ∞')


def is_bot_game():
    while True:
        try:
            is_bot = input('Хотите играть с ботом(y/n): ')
            if is_bot not in ['y', 'n']:
                raise ValueError
            return True if is_bot == 'y' else False
        except ValueError:
            print('Допустимые значения: "y" или "n"')


def player_name(nmb):
    return input(f'Введите имя {nmb} игрока: ')


def player_turn(amount, name):
    while True:
        max_cnt = max_turn_cnt if amount > max_turn_cnt else amount
        try:
            cnt = int(input(f'Ходит игрок {name}. Сколько конфет возьмёте: '))
            if cnt < min_turn_cnt or cnt > max_cnt:
                raise ValueError
            return cnt
        except ValueError:
            print(f'Допустимое значение: от {min_turn_cnt} до {max_cnt}')


def bot_turn(amount):
    return amount if amount <= max_turn_cnt else (
        amount - (min_turn_cnt + max_turn_cnt) if (amount - (min_turn_cnt + max_turn_cnt)) and
                                                  (amount - max_turn_cnt) < (min_turn_cnt + max_turn_cnt) else (
            amount % (min_turn_cnt + max_turn_cnt) if amount % (min_turn_cnt + max_turn_cnt) > 0 else min_turn_cnt
        )
    )


def turn_message(name, cnt):
    print(f'Игрок {name} взял {cnt} конфет.')


def toss_coin():
    rnd_int = randint(0, 1)
    print(f'Первым ходит игрок {player_names[rnd_int]}')
    return rnd_int


def play(amount, is_play_with_bot, first):
    play_with_bot(amount, first) if is_play_with_bot else play_with_player(amount, first)


def play_with_player(amount, who_turn_index):
    who_turn_name = player_names[who_turn_index]
    while amount > 0:
        who_turn_name = player_names[who_turn_index]
        cnt = player_turn(amount, who_turn_name)
        who_turn_index = 1 if who_turn_index == 0 else 0
        amount -= cnt
        turn_message(who_turn_name, cnt)
        print(f'На столе осталось {amount} конфет')
    print(f'Победил {who_turn_name}!')


def play_with_bot(amount, who_turn_index):
    who_turn_name = player_names[who_turn_index]
    while amount > 0:
        who_turn_name = player_names[who_turn_index]
        if who_turn_index == 0:
            cnt = player_turn(amount, who_turn_name)
            who_turn_index = 1
        else:
            cnt = bot_turn(amount)
            who_turn_index = 0
        amount -= cnt
        turn_message(who_turn_name, cnt)
        print(f'На столе осталось {amount} конфет')
    print(f'Победил {who_turn_name}!')


def main():
    candies_amount = input_candies_amount()
    is_play_with_bot = is_bot_game()
    player_names.append(player_name(1))
    player_names.append(player_name(2) if not is_play_with_bot else 'bot')
    play(candies_amount, is_play_with_bot, toss_coin())


main()
