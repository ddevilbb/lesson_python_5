# Практическое задание 3
import os
from random import randint
from time import sleep

turnX = 'X'
turnO = 'O'
turns = [str(i) for i in range(9)]
player_names = []
player_signs = [turnX, turnO]
ai_player = ''
hu_player = ''
_min = -10
_max = 10


def how_to_play():
    print(
        f'''
Чтобы сделать ход, введите число от 0 до 8, 
которое будет соответствовать номеру поля доски, показанной ниже: 
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
        '''
    )


def show_board():
    print(
        f'''
---------------------------
{' | '.join(turns[0:3:1])}
---------
{' | '.join(turns[3:6:1])}
---------
{' | '.join(turns[6:9:1])}
        '''
    )


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


def available_turns():
    global turns

    return list(filter(lambda turn: turn != turnX and turn != turnO, turns))


def player_turn(name, sign):
    while True:
        avail_turns = available_turns()
        try:
            nmb = int(input(f'Введите номер поля: '))
            if str(nmb) not in avail_turns:
                raise ValueError
            return nmb
        except ValueError:
            print(f'Допустимое значение: [{avail_turns}]')


def check_win_conditions(board, sign):
    combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in combinations:
        if sign == board[combination[0]] == board[combination[1]] == board[combination[2]]:
            return True
    return False


def bot_turn(sign):
    global ai_player, hu_player, turns

    board = turns

    ai_player = sign
    hu_player = turnO if sign == turnX else turnX

    best_move = minimax(board, ai_player, 1)

    return int(best_move['index'])


# Интеллект бота
def minimax(board, player, step):
    global ai_player, hu_player

    avail_turns = available_turns()
    if check_win_conditions(board, hu_player):
        return {
            'score': round(_min / step),
            'step': step
        }
    elif check_win_conditions(board, ai_player):
        return {
            'score': round(_max / step),
            'step': step
        }
    elif len(avail_turns) == 0:
        return {
            'score': 0,
            'step': step
        }

    moves = dict()
    for turn in avail_turns:
        move = {
            'index': board[int(turn)],
            'step': step,
        }
        board[int(turn)] = player
        result = minimax(board, (hu_player if player == ai_player else ai_player), (step + 1))
        move['score'] = result['score']
        move['step'] = result['step']

        board[int(turn)] = move['index']
        moves[len(moves)] = move
    best_move = -1
    best_score = -10000 if player == ai_player else 10000
    for i in range(len(moves)):
        if ((player == ai_player and moves[i]['score'] > best_score)
                or (player == hu_player and moves[i]['score'] < best_score)):
            best_score = moves[i]['score']
            best_move = i
    return moves[best_move] if best_move > -1 else None


def toss_coin():
    rnd_int = randint(0, 1)
    print(f'Первым ходит игрок {player_names[rnd_int]}')
    return rnd_int


def play(is_play_with_bot, first):
    play_with_bot(first) if is_play_with_bot else play_with_player(first)


def is_game_over(name, sign):
    global turns
    avail_turns = available_turns()
    if check_win_conditions(turns, sign):
        print(f'Победил {name}')
        show_board()
        return True
    if len(avail_turns) == 0:
        print('Ничья')
        show_board()
        return True
    return False


def play_with_player(who_turn_index):
    global turns
    while True:
        who_turn_name = player_names[who_turn_index]
        sign = player_signs[who_turn_index]
        print(f'Ходит игрок {who_turn_name}, знак {sign}.')
        show_board()
        turn = player_turn(who_turn_name, sign)
        if who_turn_index == 0:
            who_turn_index = 1
        else:
            who_turn_index = 0
        turns[turn] = sign
        if is_game_over(who_turn_name, sign):
            break


def play_with_bot(who_turn_index):
    global turns
    while True:
        who_turn_name = player_names[who_turn_index]
        sign = player_signs[who_turn_index]
        print(f'Ходит игрок {who_turn_name}, знак {sign}.')
        show_board()
        if who_turn_index == 0:
            turn = player_turn(who_turn_name, sign)
            who_turn_index = 1
        else:
            turn = bot_turn(sign)
            who_turn_index = 0
        turns[turn] = sign
        if is_game_over(who_turn_name, sign):
            break


def main():
    how_to_play()
    show_board()
    is_play_with_bot = is_bot_game()
    player_names.append(player_name(1))
    player_names.append(player_name(2) if not is_play_with_bot else 'bot')
    play(is_play_with_bot, toss_coin())


main()
