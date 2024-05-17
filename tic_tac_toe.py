def print_board(board):
    """Prints the game board."""
    print("\n")
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---+---+---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---+---+---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print("\n")

def check_winner(board, player):
    """Checks if the given player has won."""
    # Check rows, columns, and diagonals
    win_conditions = (
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    )
    return [player, player, player] in win_conditions

def check_draw(board):
    """Checks if the game is a draw."""
    for row in board:
        if " " in row:
            return False
    return True

def player_move(board, player):
    """Prompts the player to make a move."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                raise ValueError
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This position is already taken. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player_move(board, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break
        if check_draw(board):
            print("The game is a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

    if input("Do you want to play again? (yes/no): ").lower() == "yes":
        tic_tac_toe()
    else:
        print("Thanks for playing! Goodbye.")

# Start the game
tic_tac_toe()
