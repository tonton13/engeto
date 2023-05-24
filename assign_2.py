"""
Tic-Tac-Toe.py: a second project for Engento Online Python Academy.
author: Anton Chirkov
email: tonton.chirkov@gmail.com
discord: TonTon#9968
"""

ttt_dict = {"UL": "1", "UM": "2", "UR": "3", "CL": "4", "CM": "5", "CR": "6", "BL": "7", "BM": "8", "BR": "9"}


def get_position(val):
    for key, value in ttt_dict.items():
        if val == value:
            return key


def print_game_table():
    print("+---+---+---+")
    print(f"+{ttt_dict['UL']:^3}+{ttt_dict['UM']:^3}+{ttt_dict['UR']:^3}+")
    print("+---+---+---+")
    print(f"+{ttt_dict['CL']:^3}+{ttt_dict['CM']:^3}+{ttt_dict['CR']:^3}+")
    print("+---+---+---+")
    print(f"+{ttt_dict['BL']:^3}+{ttt_dict['BM']:^3}+{ttt_dict['BR']:^3}+")
    print("+---+---+---+")


def check_for_win(val):
    winning_combo = [
        ['UL', 'UM', 'UR'], ['CL', 'CM', 'CR'], ['BL', 'BM', 'BR'],
        ['UL', 'CL', 'BL'], ['UM', 'CM', 'BM'], ['UR', 'CR', 'BR'],
        ['UL', 'CM', 'BR'], ['UR', 'CM', 'BL']
    ]

    for combo in winning_combo:
        if all(ttt_dict[pos] == val for pos in combo):
            print(f"{val} - WON")
            quit("Game is finished")

print_game_table()

for turn in range(1, 11):
    player = 'X' if turn % 2 == 1 else "O"

    while True:
        if turn == 10:
            print("DRAW: Game is finished")
            quit("Thank you for playing")
        player_choice = input(f"PLAYER {player}: Please provide number of cell for occupation: ")
        if player_choice.isnumeric() and player_choice in ttt_dict.values():
            position = get_position(player_choice)
            ttt_dict[position] = player
            break
        elif player_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("This cell is already occupied, please choose another one.")
        elif player_choice.isnumeric() != True:
            print("input must not be a letter, please provide number of cell")
        else:
            print("Input must be exactly from 1 - 9")


    print_game_table()
    check_for_win('X')
    check_for_win('O')

