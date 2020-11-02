"""
Grid defines interactions with pyplot for display.
"""

from random import shuffle

import matplotlib.pyplot as plt

from models.board import Board


def show_grid(cfg):
    """
    Create game and setup pyplot for display.
    For pyplot, modified version of
    https://towardsdatascience.com/john-conways-game-of-life-and-interactive-visualization-9647c82044ef
    """
    # view setup
    grid_size = cfg.getProperty("grid.size")
    initial_cells = cfg.getProperty("grid.initial_cells")
    random = cfg.getProperty("grid.random")

    # game setup
    seconds_between_rounds = cfg.getProperty("game.seconds_between_rounds")
    rounds = cfg.getProperty("game.rounds")
    min_neighbor_cells = cfg.getProperty("game.min_neighbor_cells")
    max_neighbor_cells = cfg.getProperty("game.max_neighbor_cells")
    cells_to_revive = cfg.getProperty("game.cells_to_revive")

    board = Board(grid_size, min_neighbor_cells, max_neighbor_cells, cells_to_revive)
    init_and_play_board(board, random, initial_cells, rounds, seconds_between_rounds)


def init_and_play_board(board: Board, random: bool, initial_cells: int, rounds: int,
        seconds_between_rounds: float):
    """ Run the game. """
    if random:
        random_init(board, initial_cells)
    else:
        manual_init(board, initial_cells)
    play(board, rounds, seconds_between_rounds)


def manual_init(board: Board, initial_cells: int):
    """
    Click to add/remove cells.
    Stop when you've added configured number.
    """
    live_cells = 0
    while live_cells < initial_cells:
        print(f"Cells remaining to input {initial_cells - live_cells}")
        grid = plt.imshow(board.binary_grid, cmap='binary')
        click_input = plt.ginput(1, timeout=-1)
        input_col = int(round(click_input[0][1], 0))
        input_row = int(round(click_input[0][0], 0))
        if board.is_cell_alive(input_col, input_row):
            board.kill(input_col, input_row)
            live_cells -= 1
        else:
            board.make_alive(input_col, input_row)
            live_cells += 1
        board.set_grid()
        grid.set_data(board.binary_grid)
        plt.draw()


def random_init(board: Board, initial_cells: int):
    """ Start board with random cells based on config. """
    cell_ids = list(range(board.size ** 2))
    shuffle(cell_ids)
    for cell in cell_ids[:initial_cells]:
        print(int(cell / board.size), cell % board.size, cell)
        board.make_alive(int(cell / board.size), cell % board.size)
    board.set_grid()


def play(board: Board, rounds: int, seconds_between_rounds: int):
    """
    Play game for specified number of generations.
    """
    grid = plt.imshow(board.binary_grid,cmap='binary')
    while rounds > 0:
        print(f"Rounds remaining {rounds}")
        board.next_gen()
        # TO DO: check if board does not change, then end
        grid.set_data(board.binary_grid)
        plt.pause(seconds_between_rounds)
        plt.draw()
        rounds -= 1
