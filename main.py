# Importing List type from typing Python package.
from typing import List

# Create a sample board to test our function on.
board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

# Create the flood_fill function that will edit our board.
def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Check if x or y coordinate is out of bounds
    if len(input_board) < x or len(input_board[x]) < y:
        return input_board

    # Check if the current position has the old character and replace with the new character
    elif input_board[x][y] == old:
        if y == 0:
            input_board[x] = new + input_board[x][y + 1:]
        elif y == len(input_board[x]):
            input_board[x] = input_board[x][:y] + new
        else:
            input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]

        # Check the current position's surroundings (up, down, right, and left) using recursion
        flood_fill(input_board=input_board, old=old, new=new, x=x + 1, y=y)
        flood_fill(input_board=input_board, old=old, new=new, x=x - 1, y=y)
        flood_fill(input_board=input_board, old=old, new=new, x=x, y=y + 1)
        flood_fill(input_board=input_board, old=old, new=new, x=x, y=y - 1)

    # Return the input_board at the end of the recursive code.
    return input_board


if __name__ == '__main__':

    # Define the modified_board after inputting a sample board in flood_fill
    modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

    # Print out the modified_board in the Terminal:
    for a in modified_board:
        print(a)
