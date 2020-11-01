import numpy as np
from models.cell import Cell
import config_with_yaml as config
from copy import deepcopy

class Board:
    """ Game board """
    def __init__(self, size: int, min_neighbor_cells: int, max_neighbor_cells: int, cells_to_revive: int):
        # Not super memory efficient, but store two arrays
        # One with cells for logic, the other with binary values for pyplot display
        self.size = size
        self.binary_grid = np.zeros((size, size))
        self.next_binary_grid = np.zeros((size, size))
        self.cell_grid = np.empty((size, size), dtype=Cell)
        # make a copy for next gen
        self.next_cell_grid = np.empty((size, size), dtype=Cell)
        self.cells_to_update = set()
        # from config
        self.min_neighbor_cells = min_neighbor_cells
        self.max_neighbor_cells = max_neighbor_cells
        self.cells_to_revive = cells_to_revive

    def make_alive(self, x: int, y: int):
        #TO DO: ERROR CHECKING
        self.next_binary_grid[x][y] = 1
        if not self.next_cell_grid[x][y]:
            self.next_cell_grid[x][y] = Cell(x, y)
        self.next_cell_grid[x][y].make_alive()

    def kill(self, x: int, y: int):
        #TO DO: ERROR CHECKING
        self.next_binary_grid[x][y] = 0
        if not self.next_cell_grid[x][y]:
            self.next_cell_grid[x][y] = Cell(x, y)
        self.next_cell_grid[x][y].kill()

    def is_cell_alive(self, x: int, y: int) -> bool:
        return self.cell_grid[x][y].is_alive() if self.cell_grid[x][y] else False

    def get_cell(self, x: int, y: int):
        return self.cell_grid[x][y] if self.cell_grid[x][y] else Cell(x, y)

    def next_gen(self):
        # self.next_cell_grid = deepcopy(self.cell_grid)
        for x, col in enumerate(self.cell_grid):
            for y, cell in enumerate(col):
                cell = cell if cell else Cell(x, y)
                cell.live_or_die(self)
        self.cell_grid = deepcopy(self.next_cell_grid)
        self.set_grid()

    def set_grid(self):
        self.binary_grid = deepcopy(self.next_binary_grid)
        self.cell_grid = deepcopy(self.next_cell_grid)
