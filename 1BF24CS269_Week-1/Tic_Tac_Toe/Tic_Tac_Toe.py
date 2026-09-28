# Tic-Tac-Toe Human vs AI

import math

# Initialize the board
board = [' ' for _ in range(9)]

def print_board(brd):
    print()
    print(f"{brd[0]} | {brd[1]} | {brd[2]}")
    print("--+---+--")
    print(f"{brd[3]} | {brd[4]} | {brd[5]}")
    print("--+---+--")
    print(f"{brd[6]} | {brd[7]} | {brd[8]}")
    print()

def is_winner(brd, letter):
    # Check rows, columns, and diagonals
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for combo in winning_combinations:
        if brd[combo[0]] == letter and brd[combo[1]] == letter and brd[combo[2]] == letter:
            return True
    return False

def is_board_full(brd):
    return ' ' not in brd

def get_available_moves(brd):
    return [i for i, spot in enumerate(brd) if spot == ' ']

# Minimax algorithm for unbeatable AI
def minimax(brd, depth, is_maximizing):
    if is_winner(brd, 'O'):
        return 1
    if is_winner(brd, 'X'):
        return -1
    if is_board_full(brd):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(brd):
            brd[move] = 'O'
            eval_score = minimax(brd, depth + 1, False)
            brd[move] = ' '
            max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(brd):
            brd[move] = 'X'
            eval_score = minimax(brd, depth + 1, True)
            brd[move] = ' '
            min_eval = min(min_eval, eval_score)
        return min_eval

def ai_move(brd):
    best_score = -math.inf
    move = None
    for avail_move in get_available_moves(brd):
        brd[avail_move] = 'O'
        score = minimax(brd, 0, False)
        brd[avail_move] = ' '
        if score > best_score:
            best_score = score
            move = avail_move
    brd[move] = 'O'

def player_move(brd):
    run = True
    while run:
        input_num = input("Choose a position from 0 to 8: ")
        try:
            move = int(input_num)
            if move in get_available_moves(brd):
                brd[move] = 'X'
                run = False
            else:
                print("This space is occupied or invalid. Try again.")
        except ValueError:
            print("Please enter a number between 0 and 8.")

def main():
    print("\nWelcome to Tic-Tac-Toe!, Samriddha. You are 'X' and AI is 'O'.")
    print("Board positions are indexed from 0 to 8 as follows:")
    print("0 | 1 | 2")
    print("--+---+--")
    print("3 | 4 | 5")
    print("--+---+--")
    print("6 | 7 | 8")
    
    print_board(board)

    while not is_board_full(board):
        # Human turn
        if not is_winner(board, 'O'):
            player_move(board)
            print_board(board)
            if is_winner(board, 'X'):
                print("Congratulations, Samriddha! You win!")
                break
            if is_board_full(board):
                print("It's a tie!")
                break

        # AI turn
        if not is_winner(board, 'X'):
            print("AI is making a move...")
            ai_move(board)
            print_board(board)
            if is_winner(board, 'O'):
                print("AI wins! Better luck next time.")
                break
            if is_board_full(board):
                print("It's a tie!")
                break

if __name__ == "__main__":
    main()
