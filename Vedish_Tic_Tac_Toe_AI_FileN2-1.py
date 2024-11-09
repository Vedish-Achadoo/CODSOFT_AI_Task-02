#Creates a Tic-Tac-Toe board
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

#Shows the board
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

#Checks for any winner
def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

#Checks for any draw
def check_draw(board):
    return all([cell != ' ' for row in board for cell in row])

#Implement Minimax algorithm (Alpha-Beta Pruning)
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return -1
    if check_winner(board, 'X'):
        return 1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

#Vedish move using Minimax(Alpha-Beta Pruning)
def ai_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False, -float('inf'), float('inf'))
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = 'X'

#Main game loop
def play_game():
    board = create_board()
    current_player = 'O'  # Human player starts with 'O'

    while True:
        display_board(board)
        
        if current_player == 'O':
            print("Your move!")
            try:
                row = int(input("Enter row (1, 2, 3): ")) - 1
                col = int(input("Enter column (1, 2, 3): ")) - 1
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    if check_winner(board, 'O'):
                        display_board(board)
                        print("You win!")
                        break
                    current_player = 'X'
                else:
                    print("Cell already taken. Try again.")
            except IndexError:
                print("Invalid input. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Vedish's move:")
            ai_move(board)
            if check_winner(board, 'X'):
                display_board(board)
                print("Vedish wins!")
                break
            current_player = 'O'
        
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

#Starts the game
play_game()

#This is the Second task assigned by CodSoft to Vedish. Task has been completed.
#It's a Tic-Tac-Toe game with AI using Minimax algorithm and Alpha-Beta Pruning.
#Run the tool and you will be able to play Tic-Tac-Toe with the AI named Vedish.
#The AI Named Vedish will try to win Tic-Tac-Toe against you.