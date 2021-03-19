# Author: Breanna Moore
# Date: 8/11/2020
# Description: This program contains a class named FiveBoard that represents the board for a two
# player game that is like tic-tac-toe, but on a larger scale. The board is 15x15 instead of 3x3.
# Each player is trying to get 5 of their pieces in a row.

class FiveBoard:
    """
    Represents a game of tic-tac-toe with a board of 15x15. The class contains
    two private data members, a representation of the board and the current state
    of the game.
    """

    def __init__(self):
        """
        Creates a new FiveBoard object. Initializes private data members an empty
        board and current game state.
        """
        self._board = [["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]]
        self._current_state = "UNFINISHED"

    def get_current_state(self):
        """Returns current state of the game."""
        return self._current_state

    def get_board(self):
        """Prints current game board."""
        return print(self._board)

    def make_move(self, row, column, char):
        """
        Takes as a parameter two integers from 0-14 that represents the row and column
        of the game board and a string 'o' or 'x' to represent which player's turn it is.
        If the selected square of the board is already occupied, or the game has already
        been won or drawn, function returns False. Otherwise, it records the move,
        updates the current_state and returns True.
        """
        if 0 <= row <= 14 and 0 <= column <= 14 and self._current_state == "UNFINISHED":
            if char == "x" or char == "o":
                if self._board[row][column] == "":
                    self._board[row][column] = char

                    # Check if there's a winner horizontally
                    # Create list from board changing column in range -4 to 4:
                    horizontal_list = [self._board[row][column + x] for x in range(-4, 4) if 0 <= column + x < 15]
                    # Variables to track counts of O's and X's
                    horiz_count_o = 0
                    horiz_count_x = 0

                    # Count for O's and X's:
                    for y in horizontal_list:
                        if y == "o":
                            horiz_count_o += 1
                        else:
                            horiz_count_o = 0
                        if horiz_count_o == 5:
                            self._current_state = "O_WON"
                            return True
                        if y == "x":
                            horiz_count_x += 1
                        else:
                            horiz_count_x = 0
                        if horiz_count_x == 5:
                            self._current_state = "X_WON"
                            return True

                    # Check if there's a winner vertically
                    # Create list from board changing row in range -4 to 4:
                    vertical_list = [self._board[row + x][column] for x in range(-4, 4) if 0 <= row + x < 15]

                    # Variables to track counts X's and O's
                    vert_count_o = 0
                    vert_count_x = 0

                    # Count for X's and O's
                    for y in vertical_list:
                        if y == "o":
                            vert_count_o += 1
                        else:
                            vert_count_o = 0
                        if vert_count_o == 5:
                            self._current_state = "O_WON"
                            return True
                        if y == "x":
                            vert_count_x += 1
                        else:
                            vert_count_x = 0
                        if vert_count_x == 5:
                            self._current_state = "X_WON"
                            return True

                    # Check if there's a winner diagonally \
                    # Create list from board changing row and column:
                    diag_list1 = [self._board[row + x][column + x] for x in range(-4, 4) if 0 <= row + x < 15 and 0 <= column + x < 15]

                    # Variables to track count of X's and O's
                    diag_count1_o = 0
                    diag_count1_x = 0

                    # Count for X's and O's
                    for y in diag_list1:
                        if y == "o":
                            diag_count1_o += 1
                        else:
                            diag_count1_o = 0
                        if diag_count1_o == 5:
                            self._current_state = "O_WON"
                            return True
                        if y == "x":
                            diag_count1_x += 1
                        else:
                            diag_count1_x = 0
                        if diag_count1_x == 5:
                            self._current_state = "X_WON"
                            return True

                    # Check if there's a winner diagonally /
                    # Create list from board changing row and decreasing column:
                    diag_list2 = [self._board[row + x][column - x] for x in range(-4, 4) if 0 <= row + x < 15 and 0 <= column - x < 15]

                    # Variables to track counts of X's and O's
                    diag_count2_o = 0
                    diag_count2_x = 0

                    # Count for X's and O's
                    for y in diag_list2:
                        if y == "o":
                            diag_count2_o += 1
                        else:
                            diag_count2_o = 0
                        if diag_count2_o == 5:
                            self._current_state = "O_WON"
                            return True
                        if y == "x":
                            diag_count2_x += 1
                        else:
                            diag_count2_x = 0
                        if diag_count2_x == 5:
                            self._current_state = "X_WON"
                            return True

                    # Check if the game ends in a draw
                    total_count = 0
                    for row in self._board:
                        for column in row:
                            if column != "":
                                total_count += 1
                    if total_count == 225:
                        self._current_state = "DRAW"
                        return True
                    return True
        return False

