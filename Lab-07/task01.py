import copy

EMPTY = 0
WHITE = 1
BLACK = 2

def init_board():
    board = [[EMPTY for _ in range(8)] for _ in range(8)]
    for row in range(3):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = BLACK
    for row in range(5, 8):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = WHITE
    return board

def print_board(board):
    print("  " + " ".join(str(i) for i in range(8)))
    for i, row in enumerate(board):
        print(i, end=" ")
        for piece in row:
            if piece == WHITE:
                print("W", end=" ")
            elif piece == BLACK:
                print("B", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def is_valid_pos(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def get_all_valid_moves(board, player):
    captures = []
    normal_moves = []

    directions = [(-1, -1), (-1, 1)] if player == WHITE else [(1, -1), (1, 1)]

    for i in range(8):
        for j in range(8):
            if board[i][j] != player:
                continue
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if is_valid_pos(ni, nj) and board[ni][nj] == EMPTY:
                    normal_moves.append(((i, j), (ni, nj)))
                elif is_valid_pos(ni, nj) and board[ni][nj] != player and board[ni][nj] != EMPTY:
                    ci, cj = i + 2 * dx, j + 2 * dy
                    if is_valid_pos(ci, cj) and board[ci][cj] == EMPTY:
                        captures.append(((i, j), (ci, cj)))

    return captures if captures else normal_moves

def make_move(board, move):
    new_board = copy.deepcopy(board)
    (x1, y1), (x2, y2) = move
    player = new_board[x1][y1]
    new_board[x1][y1] = EMPTY
    new_board[x2][y2] = player
    if abs(x2 - x1) == 2:
        cap_x, cap_y = (x1 + x2) // 2, (y1 + y2) // 2
        new_board[cap_x][cap_y] = EMPTY
    return new_board

def evaluate_board(board):
    white_score = sum(row.count(WHITE) for row in board)
    black_score = sum(row.count(BLACK) for row in board)
    return black_score - white_score

def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0 or is_game_over(board):
        return evaluate_board(board), None

    player = BLACK if maximizing else WHITE
    best_move = None
    moves = get_all_valid_moves(board, player)

    if maximizing:
        max_eval = float('-inf')
        for move in moves:
            eval, _ = minimax(make_move(board, move), depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in moves:
            eval, _ = minimax(make_move(board, move), depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def is_game_over(board):
    return len(get_all_valid_moves(board, WHITE)) == 0 or len(get_all_valid_moves(board, BLACK)) == 0

def get_winner(board):
    white_left = sum(row.count(WHITE) for row in board)
    black_left = sum(row.count(BLACK) for row in board)
    if white_left == 0 or len(get_all_valid_moves(board, WHITE)) == 0:
        return "AI wins!"
    elif black_left == 0 or len(get_all_valid_moves(board, BLACK)) == 0:
        return "Player wins!"
    else:
        return "Draw!"

def play_game():
    board = init_board()
    print("Welcome to Checkers! You are WHITE (W), AI is BLACK (B)")
    turn = 'human'

    while not is_game_over(board):
        print_board(board)

        if turn == 'human':
            print("Your turn.")
            moves = get_all_valid_moves(board, WHITE)
            if not moves:
                break
            while True:
                try:
                    print("Enter your move in format: x1 y1 x2 y2")
                    x1, y1, x2, y2 = map(int, input("Your move: ").split())
                    if ((x1, y1), (x2, y2)) in moves:
                        board = make_move(board, ((x1, y1), (x2, y2)))
                        print(f"Player moves: ({x1},{y1}) → ({x2},{y2})")
                        break
                    else:
                        print("Invalid move. Try again.")
                except:
                    print("Invalid input. Use format: x1 y1 x2 y2")
            turn = 'ai'

        else:
            print("AI is thinking...")
            _, move = minimax(board, 4, float('-inf'), float('inf'), True)
            if move:
                x1, y1 = move[0]
                x2, y2 = move[1]
                board = make_move(board, move)
                print(f"AI moves: ({x1},{y1}) → ({x2},{y2})")
            else:
                print("AI has no moves.")
            turn = 'human'

    print_board(board)
    print("Game Over!", get_winner(board))

if __name__ == "__main__":
    play_game()
