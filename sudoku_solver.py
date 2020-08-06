"""The solver uses backtracking algorithm to solve the board.

'Three keys to backtracking:
 1. Choice
 2. Constrains
 3. Goal'

source: 'Back to Back SWE' - YouTube channel.
[https://www.youtube.com/channel/UCmJz2DV1a3yfgrR7GqRtUUA]

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

    def solver(self, row, col):
        """Main function used to solve the board.
        The function solves the board row-wise.

        Args:
            row (int): row number.
            col (int): column number.

        Returns:
            (bool): 'True' if the number does not break any of the constrains.
        """
        # TODO: Create a breakpoint for end of the row.
        # TODO: Create a condition to know board is solved

        # TODO: Fill cell and check if constrains violated

        # TODO: Remove entry if constrains violated.
        pass

    def set_board(self, array):
        """Sets up the board with the input array.
        The array is converted to a numpy array.

        Notes:
            The empty cells are to be filled with the value '0's.

        Args:
            array (9x9 matrix): Can in the form of lists or tuples.

        Returns: None
        """
        # TODO: Add check for right array dimensions
        self.board = np.array(array)

    def valid_board(self):
        """Checks if the current board follows all the constrains.

        Args: None

        Returns:
            (bool): Is the board is solved. True if all constrains are met.
            (int): Row, Column or Block number where there is an error.
        """
        # TODO: Raise an error if the board is not complete.
        if 0 in self.board:
            pass

        for i in range(9):
            is_valid = self.has_only_unique(self.board[i, :],  # row check
                                            self.board[:, i],  # col check
                                            self.blocks[i])    # block check
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
            ignore (tuple of int): the integer values to be ignored.

        Returns:
            (bool): Are all the values unique? (Ignoring the values in ignore)
                    True if there are no duplicate values.
        """
        # TODO: Add check for the type of *args.
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

    def set_blocks(self):
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

