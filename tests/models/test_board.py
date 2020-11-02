"""
Test board class.

Also exercises all cell functionality.
"""

import pytest

from models.board import Board

def test_board_init_errors():
    """ Check that invalid inits raise exceptions """
    with pytest.raises(Exception):
        # negative size
        Board(-1, 2, 3, 3)
    with pytest.raises(Exception):
        # negative min_neighbor
        Board(1, -2, 3, 3)
    with pytest.raises(Exception):
        # negative max_neighbor
        Board(1, 2, -3, 3)
    with pytest.raises(Exception):
        # max less than min
        Board(1, 3, 2, 3)
    with pytest.raises(Exception):
        # negative cells to revive
        Board(1, 2, 3, -3)

def test_board_init_make_alive_and_kill():
    """ Check that you can make alive then kill a cell """
    board = Board(4, 2, 3, 3)
    board.make_alive(1, 1)
    board.set_grid()
    assert board.is_cell_alive(1, 1)
    board.kill(1, 1)
    board.set_grid()
    assert not board.is_cell_alive(1, 1)

def test_board_get_cell_ok():
    """ Can get cell either by default or if already exists """
    board = Board(4, 2, 3, 3)
    cell = board.get_cell(1, 1)
    # if cell isnt yet assigned is not alive
    assert not cell.is_alive()
    board.make_alive(1, 1)
    board.set_grid()
    cell = board.get_cell(1, 1)
    # cell is assigned and is alive
    assert cell.is_alive()

def test_board_revive_cell():
    """ Test that a cell can be revived """
    board = Board(4, 2, 3, 3)
    board.make_alive(1, 1)
    board.make_alive(1, 2)
    board.make_alive(1, 3)
    board.set_grid()
    board.next_gen()
    assert board.get_cell(2, 2).is_alive()

def test_board_get_cell_error():
    """ Cannot get cell outside range of cells """
    board = Board(4, 2, 3, 3)
    with pytest.raises(IndexError):
        board.get_cell(10, 10)

def test_next_gen_with_cells():
    """ Check next_gen with set of cells to check. """
    board = Board(4, 2, 3, 3)
    board.make_alive(1, 1)
    board.set_grid()
    board.cells_to_check = set()
    board.cells_to_check.add((1, 1))
    board.next_gen()
    # single cell should die
    assert not board.get_cell(1, 1).is_alive()

def test_next_gen_with_bad_cell_to_check():
    """ Check next_gen with set of cells to check. """
    board = Board(4, 2, 3, 3)
    board.make_alive(1, 1)
    board.set_grid()
    board.cells_to_check = set()
    board.cells_to_check.add((10, 10))
    with pytest.raises(IndexError):
        board.next_gen()

def test_next_gen_without_cells():
    """ Check next_gen checking all cells. """
    board = Board(4, 2, 3, 3)
    board.make_alive(1, 1)
    board.set_grid()
    board.next_gen()
    # single cell should die
    assert not board.get_cell(1, 1).is_alive()

def test_various_index_errors():
    """ Some things that won'f work with input outside grid. """
    board = Board(4, 2, 3, 3)
    with pytest.raises(IndexError):
        board._Board__init_next_gen(10, 10)
    with pytest.raises(IndexError):
        board._Board__update_binary_grid(10, 10, 1)
    with pytest.raises(IndexError):
        board._Board__revive_next_gen(10, 10)
