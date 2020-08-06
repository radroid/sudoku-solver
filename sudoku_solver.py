"""The solver uses backtracking algorithm to solve the board.

'Three keys to backtracking:
 1. Choice
 2. Constrains
 3. Goal'

source: 'Back to Back SWE' - YouTube channel.
[https://www.youtube.com/channel/UCmJz2DV1a3yfgrR7GqRtUUA]

 * The video is just a reference, the code used here is not a copy of it. It is
   written with my understanding of backtracking.

The algorithm uses recursion to solve the board in a more efficient way than
going through all the possibilities.
"""
import numpy as np


class SudokuSolver:
    """The class contains variables and methods needed to solve the sudoku
    board.

    Attributes:
        board (nd_array): contains the sudoku board.
        blocks (list of nd_arrays): contains the square blocks of the sudoku
                                   board.
    """

    def __init__(self):
        """Instantiates object"""
        self.blocks = []
        self.board = np.array([])

    def solve_board(self, row=0, col=0):
        """Main function used to solve the board.
        The function solves the board row-wise.

        Args:
            row (int): row number (index starts from 0).
            col (int): column number (index starts from 0).

        Returns:
            (bool): 'True' if the number does not break any of the constrains.
        """
        if row == 9:
            return True

        if col == 9:
            return self.solve_board(row + 1, 0)
        elif self.board[row, col] != 0:
            return self.solve_board(row, col + 1)
        else:
            for i in range(1, 10):
                self.update_board(row, col, i)

                if self.valid_entry(row, col):
                    if self.solve_board(row, col + 1):
                        return True

            self.update_board(row, col, 0)

    def set_board(self, array):
        """Sets up the board with the input array.
        The array is converted to a numpy array.

        Notes:
            The empty cells are to be filled with the value '0's.

        Args:
            array (9x9 matrix): Can in the form of lists or tuples.

        Returns: None
        """
        if not (len(array), len(array[0])) == (9, 9):
            raise UserWarning("The array input is not of valid dimensions.")

        self.board = np.array(array)
        self.__set_blocks()

    def valid_board(self):
        """Checks if the current board follows all the constrains.

        Args: None

        Returns:
            (bool): Is the board is solved. True if all constrains are met.
            (int): Row, Column or Block number where there is an error.
        """
        if 0 in self.board:
            raise UserWarning("The board is not complete as there are 0's "
                              "present on the board.")

        for i in range(9):
            is_valid = self.has_only_unique(
                self.board[i, :].tolist(),              # row check
                self.board[:, i].tolist(),              # col check
                self.blocks[i].reshape(1, 9).tolist())  # block check
            if not is_valid:
                return False, i

        return True

    def valid_entry(self, row, col):
        """Checks whether the entry provided meets the constrains or no.

        Notes:
            - The values of row and col start index from 0. Hence range from
              0 to 8, including 0 and 8.
            - The calculation to determine the block_num uses simple logic and
              understanding of the structure of blocks.

        Args:
            row (int): the row number of the entry (ideally the last entry)
            col (int): the column number of the entry (ideally the last entry)

        Returns:
            (bool): Is the entry valid. True if all constrains are met.
        """
        board_row = self.board[row, :].tolist()
        board_col = self.board[:, col].tolist()

        # Determining the block location and converting the block to a list.
        block_num = col // 3 + (row // 3) * 3
        block = self.blocks[block_num].reshape(1, 9)[0].tolist()
        return self.has_only_unique(board_row, board_col, block)

    @staticmethod
    def has_only_unique(*list_of_nums, ignore=(0,)):
        """Checks if the list of numbers input has only unique values.
        Ignores value 0.

        Args:
            *list_of_nums (iterable of int): Can be any number of iterables
                                             containing the numbers of the
                                             checked.
            ignore (tuple of int): the integer values to be ignored.

        Returns:
            (bool): Are all the values unique? (Ignoring the values in ignore)
                    True if there are no duplicate values.
        """
        for num_list in list_of_nums:
            values = []
            for num in num_list:
                if num in ignore:
                    continue
                if num in values:
                    return False
                else:
                    values.append(num)
        return True

    def __set_blocks(self):
        """Sets up nine blocks as seen on a Sudoku board."""
        blocks = []
        board = self.board
        for i_row, j_row in zip(range(0, 7, 3), range(3, 10, 3)):
            for i_col, j_col in zip(range(0, 7, 3), range(3, 10, 3)):
                blocks.append(board[i_row:j_row, i_col:j_col])

        self.blocks = blocks

    def update_board(self, row, col, value):
        """Updates the board and blocks attributes of the object.

        Args:
            row (int): row number
            col (int): column number
            value (int): value to be saved in place of the current value.

        Returns: None
        """
        self.board[row, col] = value

        # Calculating the location in blocks of the corresponding value.
        block_num = col // 3 + (row // 3) * 3
        b_row, b_col = row - (row // 3 * 3), col - (col // 3 * 3)

        self.blocks[block_num][b_row, b_col] = value
