# Q3


## Agent Description:

The agent is a computer program that plays chess using AI against humans. It examines the current board, determines potential moves, and selects the best move based on learned procedures.

## Description of its Surroundings:

- **Perceivability:** Yes. The agent knows the whole chessboard and the position of all pieces at any moment.
- **Deterministic:** Yes. Chess is deterministic since all movements have a predefined result and nothing is random.
- **Episodic:** No. The game is sequential, hence non-episodic.
- **Static:** Yes. The board remains static until a move is made.
Board state is updated after each player's turn.
- **Continuous:** No. Chess is not continuous. It has separate steps, with a finite number of legal moves at any moment.

## Best Agent Design:

1. **Search Algorithms:** Minimax with Alpha-Beta Pruning helps to look at possible moves and choose the best one by checking future outcomes.
2. **Heuristic Evaluation Functions:** They give ratings to board positions by features such as material gain, piece activity, king safety, etc.
3. **Reinforcement Learning:** Neural networks (Alpha Zero) learn strategies playing against themselves.
