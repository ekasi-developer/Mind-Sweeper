import unicode
import board
from game_state import GameState


# Initialize GameState to key track if the game has ended.
game_state = GameState()

print(" Welcome to WeThinkCode (Group 26) MineSweeper.\n\n"
      "-----------------------------------------------------------\n"
      "| Rules:" + (" " * 50) + "|\n"
      "-----------------------------------------------------------\n"
      f"| * Number of rows must be greater then or equal to {board.MIN_NUMBER_COLUMNS}." + (" " * 4) + "|\n"
      f"| * Number of columns must be greater then or equal to {board.MIN_NUMBER_ROWS}. |\n"
      "| * Rows " + unicode.ARROW_DOWN + (" " * 48) + "|\n"
      "| * Columns " + unicode.ARROW_RIGHT + (" " * 45) + "|\n"
      "-----------------------------------------------------------\n")

columns = int(input("Enter the number of columns: "))
rows = int(input("Enter the number of rows: "))

if columns < board.MIN_NUMBER_COLUMNS and rows < board.MIN_NUMBER_ROWS:
    print(f"Please re-enter the correct number of rows or columns.")
    exit()

game_board = board.generate(columns, rows)
display_board = board.generate(columns, rows, True)


def copy_box(board: list, row: int, column: int, value: int) -> list:
    board[row][column] = value
    return board


while game_state.state():
    print(board.display(display_board))
    selected_row = int(input("Select row: "))
    if board.row_exists(game_board, selected_row) is False:
        print(f"The row selected ({selected_row}) row does not exists.\n\n")
        continue
    selected_column = int(input("Select column: "))
    if board.column_exists(game_board, selected_column) is False:
        print(f"The column ({selected_column}) selected does not exists.\n\n")
        continue
    opened_box = board.make_move(game_board, selected_row, selected_column)
    if board.is_bomb(opened_box):
        print(board.display(game_board))
        print(f"Sorry you have opened a bomb " + unicode.BOOM)
        exit()
    display_board = copy_box(display_board, selected_row, selected_column, opened_box)
