"""
Test grid setup
"""

from doubles import allow
import config_with_yaml as config

from models.board import Board
from views import grid


def test_show_grid():
    class DummyGrid:
        def set_data(self, data):
            pass

    cfg = config.load("config.yaml")
    allow(grid).init_and_play_board.and_return(None)
    grid.show_grid(cfg)


def test_init_and_play_random():
    board = Board(4, 2, 3, 3)
    grid.init_and_play_board(board, True, 1, 1, .1)
    # single cell should die
    for row in board.cell_grid:
        for cell in row:
            assert not cell or not cell.is_alive()


def test_init_and_play_manual():
    board = Board(4, 2, 3, 3)
    allow(grid.plt).ginput.and_return(((1, 1), (0, 0)))
    grid.init_and_play_board(board, False, 1, 1, .1)
    # single cell should die
    for row in board.cell_grid:
        for cell in row:
            assert not cell or not cell.is_alive()
