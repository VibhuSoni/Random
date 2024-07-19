import sys

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def get_move(player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column): ")
            row, col = map(int, move.split())
            if row in range(1, 4) and col in range(1, 4):
                return row - 1, col - 1
            else:
                print("Invalid input. Please enter row and column between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row, col = get_move(current_player)

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Cell already taken. Choose another one.")
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
