import board
from game_state import GameState


# Initialize Game State
game_state = GameState()

print("Welcome to WeThinkCode (Group 26) MineSweeper\n"
      "Rules:\n"
      f"Min Columns {board.MIN_NUMBER_COLUMNS}\n"
      f"Min Rows {board.MIN_NUMBER_ROWS}\n")

columns = 4  # int(input("Enter the number of columns: "))
rows = 4  # int(input("Enter the number of rows: "))


if columns < board.MIN_NUMBER_COLUMNS and rows < board.MIN_NUMBER_ROWS:
    print(f"Please re-enter the correct number of rows or columns.")
    exit()

game_board = board.generate(columns, rows)
sample_board = board.generate(columns, rows, True)


while game_state.state():
      pass








# print(board.display(game_board))
# print(board.display(sample_board))


