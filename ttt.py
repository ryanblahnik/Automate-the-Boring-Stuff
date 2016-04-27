import random, copy

def draw_board(board):
    print(board['t_l'] + '|' + board['t_c'] + '|' + board['t_r'])
    print('-----')
    print(board['c_l'] + '|' + board['c_c'] + '|' + board['c_r'])
    print('-----')
    print(board['b_l'] + '|' + board['b_c'] + '|' + board['b_r'])

def input_player_letter():
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def who_goes_first():
    if player_letter == 'X':
        return 'player'
    else:
        return 'computer'

def play_again():
    print('Do you want to play again (yes or no)?')
    return input().lower().startswith('y')

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    return ((bo['t_l'] == le and bo['t_c'] == le and bo['t_r'] == le) or
    (bo['c_l'] == le and bo['c_c'] == le and bo['c_r'] == le) or
    (bo['b_l'] == le and bo['b_c'] == le and bo['b_r'] == le) or
    (bo['t_l'] == le and bo['c_l'] == le and bo['b_l'] == le) or
    (bo['t_c'] == le and bo['c_c'] == le and bo['b_c'] == le) or
    (bo['t_r'] == le and bo['c_r'] == le and bo['b_r'] == le) or
    (bo['t_l'] == le and bo['c_c'] == le and bo['b_r'] == le) or
    (bo['b_l'] == le and bo['c_c'] == le and bo['t_r'] == le))

def is_space_free(board, move):
    return board[move] == ' '

def get_player_move(board):
    move = ' '
    while move not in 't_l t_c t_r c_l c_c c_r b_l b_c b_r'.split() or not is_space_free(board, move):
        print('Where do you want to go next? (t_, c_, b_ and l, c, r)')
        move = input()
    return move

def choose_random_move_from_list(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def get_computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    for i in 't_l t_c t_r c_l c_c c_r b_l b_c b_r'.split():
        dupe = copy.copy(board)
        if is_space_free(dupe, i):
            make_move(dupe, computer_letter, i)
            if is_winner(dupe, computer_letter):
                return i

    for i in 't_l t_c t_r c_l c_c c_r b_l b_c b_r'.split():
        dupe = copy.copy(board)
        if is_space_free(dupe, i):
            make_move(dupe, player_letter, i)
            if is_winner(dupe, player_letter):
                return i

    move = choose_random_move_from_list(board, ['t_l', 't_r', 'b_l', 'b_r'])
    if move != None:
        return move

    if is_space_free(board, 'c_c'):
        return 'c_c'

    return choose_random_move_from_list(board, ['t_c', 'b_c', 'c_l', 'c_r'])

def is_board_full(board):
    for i in 't_l t_c t_r c_l c_c c_r b_l b_c b_r'.split():
        if is_space_free(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe')
print('')


while True:
    the_board = {'t_l': ' ', 't_c': ' ', 't_r': ' ',
                 'c_l': ' ', 'c_c': ' ', 'c_r': ' ',
                 'b_l': ' ', 'b_c': ' ', 'b_r': ' '}
    draw_board(the_board)
    print('')
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print('')
    print('The ' + turn + ' will go first.')
    print('')
    game_is_playing = True

    while game_is_playing:
        if turn == 'player':
            print('')
            draw_board(the_board)
            print('')
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                print('')
                draw_board(the_board)
                print('')
                print('You have won the game!')
                print('')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    print('')
                    draw_board(the_board)
                    print('')
                    print('The game is a tie!')
                    print('')
                    break
                else:
                    turn = 'computer'

        else:
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                print('')
                draw_board(the_board)
                print('')
                print('The computer wins! You lost..')
                print('')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    print('')
                    draw_board(the_board)
                    print('')
                    print('The game is a tie!')
                    print('')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
