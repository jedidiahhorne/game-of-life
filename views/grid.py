# TO DO: confirm input order
# TO DO: UNIT TESTS/LINT
# TO DO: optimize cells to review
# TO DO: stop when repeat loop
import numpy as np
import matplotlib.pyplot as plt
from models.board import Board
from random import shuffle

# pyplot grid is modified version of
# https://towardsdatascience.com/john-conways-game-of-life-and-interactive-visualization-9647c82044ef
def show_grid(board_size: int, initial_cells: int, rounds: int,
              seconds_between_rounds: int, random: bool, min_neighbor_cells :int,
              max_neighbor_cells: int, cells_to_revive: int):
    board = Board(board_size, min_neighbor_cells, max_neighbor_cells, cells_to_revive)
    if random:
        random_init(board, initial_cells)
    else:
        manual_init(board, initial_cells)
    play(board, rounds, seconds_between_rounds)

def manual_init(board: Board, initial_cells: int):
    """ Stop when you've added configured number of live cells """
    live_cells = 0
    while live_cells < initial_cells:
        print(f"Cells remaining to input {initial_cells - live_cells}")
        grid = plt.imshow(board.binary_grid,cmap='binary')
        pt = plt.ginput(1, timeout=-1)
        p_1 = int(round(pt[0][1],0))
        p_2 = int(round(pt[0][0],0))
        coord = (p_2,len(board.binary_grid)-p_1-1)
        if board.is_cell_alive(p_1, p_2):
            board.kill(p_1, p_2)
            live_cells -= 1
        else:
            board.make_alive(p_1, p_2)
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
    grid = plt.imshow(board.binary_grid,cmap='binary')
    while rounds > 0:
        print(f"Rounds remaining {rounds}")
        board.next_gen()
        # TO DO: check if board does not change, then end
        grid.set_data(board.binary_grid)
        plt.pause(seconds_between_rounds)
        plt.draw()
        # input("Press Enter to continue ...")
        rounds -= 1
    input("Press Enter to continue...")