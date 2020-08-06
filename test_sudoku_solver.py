"""Tests for the sudoku solver."""


from sudoku_solver import SudokuSolver
from pytest import raises

solver = SudokuSolver()

prob_array = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
              [6, 8, 0, 0, 7, 0, 0, 9, 0],
              [1, 9, 0, 0, 0, 4, 5, 0, 0],
              [8, 2, 0, 1, 0, 0, 0, 4, 0],
              [0, 0, 4, 6, 0, 2, 9, 0, 0],
              [0, 5, 0, 0, 0, 3, 0, 2, 8],
              [0, 0, 9, 3, 0, 0, 0, 7, 4],
              [0, 4, 0, 0, 5, 0, 0, 3, 6],
              [7, 0, 3, 0, 1, 8, 0, 0, 0]]

sol_array = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
             [6, 8, 2, 5, 7, 1, 4, 9, 3],
             [1, 9, 7, 8, 3, 4, 5, 6, 2],
             [8, 2, 6, 1, 9, 5, 3, 4, 7],
             [3, 7, 4, 6, 8, 2, 9, 1, 5],
             [9, 5, 1, 7, 4, 3, 6, 2, 8],
             [5, 1, 9, 3, 2, 6, 8, 7, 4],
             [2, 4, 8, 9, 5, 7, 1, 3, 6],
             [7, 6, 3, 4, 1, 8, 2, 5, 9]]

wrong_array = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
               [6, 8, 2, 5, 7, 1, 4, 9, 3],
               [1, 9, 7, 8, 3, 4, 5, 6, 2],
               [8, 2, 6, 1, 9, 5, 3, 4, 7],
               [3, 7, 4, 6, 8, 2, 9, 1, 5],
               [9, 5, 1, 7, 4, 3, 6, 2, 8],
               [5, 1, 9, 3, 2, 6, 8, 7, 4],
               [2, 4, 8, 9, 5, 7, 1, 3, 6],
               [7, 6, 3, 4, 1, 8, 2, 5, 5]]


def test_board():
    solver.set_board(prob_array)
    truth_mat = solver.board == prob_array
    assert truth_mat.all()


def test_valid_board_wrong_1():
    solver.set_board(prob_array)
    with raises(UserWarning):
        solver.valid_board()


def test_valid_board_right():
    solver.set_board(sol_array)
    assert solver.valid_board()


def test_valid_board_wrong_2():
    solver.set_board(wrong_array)
    result = solver.valid_board()
    assert not result[0]


def setup_prob():
    """Sets up the board to be tested for the next four tests of
    has_only_unique."""
    solver.set_board(prob_array)


def test_has_only_unique_true_1():
    setup_prob()
    block1 = solver.blocks[0].reshape(1, 9)[0].tolist()
    block2 = solver.blocks[3].reshape(1, 9)[0].tolist()
    assert solver.has_only_unique(block1, block2)


def test_has_only_unique_true_2():
    setup_prob()
    block1 = solver.blocks[0].reshape(1, 9)[0].tolist()
    block2 = [9, 1, 4, 2, 5, 6, 6, 7, 8]
    assert solver.has_only_unique(block1, block2, ignore=(0, 6))


def test_has_only_unique_false_1():
    setup_prob()
    block1 = solver.blocks[0].reshape(1, 9)[0].tolist()
    block2 = solver.blocks[3].reshape(1, 9)[0].tolist()
    assert not solver.has_only_unique(block1, block2, ignore=())


def test_has_only_unique_false_2():
    setup_prob()
    block1 = solver.blocks[0].reshape(1, 9)[0].tolist()
    block2 = [9, 1, 4, 2, 5, 6, 6, 7, 8]
    assert not solver.has_only_unique(block1, block2)


def test_solver():
    setup_prob()
    solver.solve_board(0, 0)
    result = solver.board == sol_array
    assert result.all()
