def minimax(cards, left, right, is_max_turn, alpha, beta):
    if left > right:
        return 0

    if is_max_turn:
        pick_left = cards[left] + minimax(cards, left + 1, right, False, alpha, beta)
        pick_right = cards[right] + minimax(cards, left, right - 1, False, alpha, beta)
        best = max(pick_left, pick_right)
        alpha = max(alpha, best)
        if beta <= alpha:
            return best
        return best
    else:
        if cards[left] < cards[right]:
            return minimax(cards, left + 1, right, True, alpha, beta)
        else:
            return minimax(cards, left, right - 1, True, alpha, beta)

def play_game(cards):
    max_score = 0
    min_score = 0
    left = 0
    right = len(cards) - 1
    turn = "Max"

    print(f"Initial Cards: {cards}")

    while left <= right:
        if turn == "Max":
            pick_left = cards[left] + minimax(cards, left + 1, right, False, float('-inf'), float('inf'))
            pick_right = cards[right] + minimax(cards, left, right - 1, False, float('-inf'), float('inf'))

            if pick_left >= pick_right:
                choice = cards[left]
                left += 1
            else:
                choice = cards[right]
                right -= 1
            max_score += choice
            print(f"Max picks {choice}, Remaining Cards: {cards[left:right+1]}")
            turn = "Min"
        else:
            if cards[left] < cards[right]:
                choice = cards[left]
                left += 1
            else:
                choice = cards[right]
                right -= 1
            min_score += choice
            print(f"Min picks {choice}, Remaining Cards: {cards[left:right+1]}")
            turn = "Max"

    print(f"\nFinal Scores - Max: {max_score}, Min: {min_score}")
    if max_score > min_score:
        print("Winner: Max")
    elif min_score > max_score:
        print("Winner: Min")
    else:
        print("It's a tie!")

cards = [4, 10, 6, 2, 9, 5]
play_game(cards)
