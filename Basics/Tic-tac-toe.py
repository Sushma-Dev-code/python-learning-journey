def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(board, player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False


def tic_tac_toe():
    board = ["1","2","3","4","5","6","7","8","9"]
    current_player = "X"

    for turn in range(9):
        print_board(board)

        try:
            choice = int(input(f"Player {current_player}, choose position (1-9): ")) - 1

            if board[choice] not in ["X","O"]:
                board[choice] = current_player
            else:
                print("Position already taken!")
                continue

        except:
            print("Invalid input!")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} Wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a Draw!")


if __name__ == "__main__":
    tic_tac_toe()