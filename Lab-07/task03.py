import random

GRID_SIZE = 10
SHIP_SIZES = [5, 4, 3, 3, 2]

def create_board():
    return [["~"] * GRID_SIZE for _ in range(GRID_SIZE)]

def print_board(board, hide_ships=True):
    print("  " + " ".join("ABCDEFGHIJ"))
    for i, row in enumerate(board):
        display = [cell if not hide_ships or cell in ["X", "O"] else "~" for cell in row]
        print(str(i) + " " + " ".join(display))

def place_ship(board, size):
    while True:
        orientation = random.choice(["H", "V"])
        if orientation == "H":
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - size)
            if all(board[row][col + i] == "~" for i in range(size)):
                for i in range(size):
                    board[row][col + i] = "S"
                return
        else:
            row = random.randint(0, GRID_SIZE - size)
            col = random.randint(0, GRID_SIZE - 1)
            if all(board[row + i][col] == "~" for i in range(size)):
                for i in range(size):
                    board[row + i][col] = "S"
                return

def place_all_ships(board):
    for size in SHIP_SIZES:
        place_ship(board, size)

def parse_input(inp):
    if len(inp) < 2 or inp[0] not in "ABCDEFGHIJ" or not inp[1:].isdigit():
        return None
    col = ord(inp[0]) - ord('A')
    row = int(inp[1:])
    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
        return row, col
    return None

def is_game_over(board):
    for row in board:
        if "S" in row:
            return False
    return True

def attack(board, row, col):
    if board[row][col] == "S":
        board[row][col] = "X"
        return "Hit!"
    elif board[row][col] == "~":
        board[row][col] = "O"
        return "Miss"
    elif board[row][col] in ["X", "O"]:
        return "Already tried"
    return "Error"

ai_hits = []

def ai_guess(board):
    global ai_hits
    if ai_hits:
        last_hit = ai_hits[-1]
        r, c = last_hit
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE and board[nr][nc] in ["~", "S"]:
                return nr, nc
    while True:
        r = random.randint(0, GRID_SIZE - 1)
        c = random.randint(0, GRID_SIZE - 1)
        if board[r][c] in ["~", "S"]:
            return r, c

def play_battleship():
    player_board = create_board()
    ai_board = create_board()
    place_all_ships(player_board)
    place_all_ships(ai_board)

    print("Welcome to Battleship!")
    while True:
        print("\nYour Board:")
        print_board(player_board, hide_ships=False)
        print("\nEnemy Board:")
        print_board(ai_board)

        while True:
            move = input("Enter attack coordinate (e.g., B4): ").upper()
            coord = parse_input(move)
            if coord:
                r, c = coord
                result = attack(ai_board, r, c)
                if result == "Already tried":
                    print("You've already attacked that spot. Try again.")
                else:
                    print(f"Player attacks: {move} → {result}")
                    if result.startswith("Hit"):
                        ai_board[r][c] = "X"
                    break
            else:
                print("Invalid input. Try again.")

        if is_game_over(ai_board):
            print("You win! All AI ships sunk.")
            break

        r, c = ai_guess(player_board)
        result = attack(player_board, r, c)
        print(f"AI attacks: {chr(c + ord('A'))}{r} → {result}")
        if result == "Hit!":
            ai_hits.append((r, c))

        if is_game_over(player_board):
            print("AI wins! All your ships are sunk.")
            break

play_battleship()
