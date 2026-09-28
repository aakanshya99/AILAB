import math

board = [" "] * 9


def print_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()


def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    if " " not in board:
        return "Tie"

    return None


def minimax(is_maximizing):
    result = check_winner()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Tie":
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def best_move():
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


# Game loop
print("Tic-Tac-Toe!")
print("You are X. AI is O.")
print("Positions are numbered 1-9:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")

while True:
    print_board()

    # Human move
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                break

            print("Invalid move. Try again.")

        except ValueError:
            print("Enter a number from 1 to 9.")

    result = check_winner()

    if result:
        print_board()
        if result == "Tie":
            print("It's a tie!")
        else:
            print(f"{result} wins!")
        break

    # AI move
    ai_move = best_move()
    board[ai_move] = "O"

    print(f"AI chooses position {ai_move + 1}")

    result = check_winner()

    if result:
        print_board()
        if result == "Tie":
            print("It's a tie!")
        else:
            print(f"{result} wins!")
        break
