"""
A board holds three numpy arrays:
(1) a binary grid for pyplot display in view
(2) a grid of cells containing live/die logic
(3) a grid of new modified cells holding next generation state
"""

from copy import deepcopy

import numpy as np

from models.cell import Cell


class Board:
    """ Game board """
    def __init__(self, size: int, min_neighbor_cells: int,
                 max_neighbor_cells: int, cells_to_revive: int) -> None:
        # check config conditions
        if size <= 0:
            raise Exception("Board size must be positive.")
        if min_neighbor_cells < 0 or max_neighbor_cells < 0:
            raise Exception("Must have positive values for growth conditions.")
        if min_neighbor_cells > max_neighbor_cells:
            raise Exception("Max cells to live must be greater than min cells.")
        # Not super memory efficient, but store two arrays
        # One with cells for logic, the other with binary values for pyplot display
        self.size = size
        self.binary_grid = np.zeros((size, size))
        self.cell_grid = np.empty((size, size), dtype=Cell)
        # make a copy for next gen
        self.next_cell_grid = np.empty((size, size), dtype=Cell)
        self.cells_to_update = set()
        # from config
        self.game_config = {
            "min_live": min_neighbor_cells,
            "max_live": max_neighbor_cells,
            "revive": cells_to_revive,
        }
        self.cells_to_check = None

    def make_alive(self, col: int, row: int) -> None:
        """ Update binary grid and temporary board for next gen """
        self.__update_binary_grid(col, row, 1)
        self.__revive_next_gen(col, row)

    def kill(self, col: int, row: int) -> None:
        """ Update binary grid and temporary board for next gen """
        self.__update_binary_grid(col, row, 0)
        self.__kill_next_gen(col, row)

    def is_cell_alive(self, col: int, row: int) -> bool:
        """ Is cell alive """
        return self.cell_grid[col][row].is_alive() if self.cell_grid[col][row] else False

    def get_cell(self, col: int, row: int) -> None:
        """ Get cell """
        try:
            return self.cell_grid[col][row] if self.cell_grid[col][row] else Cell(col, row)
        except IndexError:
            print(f"Tried to update {col} {row} outside of grid size {self.size}")
            raise

    def next_gen(self) -> None:
        """ Using either cells to check or full grid, kill/revive cells. """
        if self.cells_to_check:
            print(f"Checking {len(self.cells_to_check)} cells from previous generation.")
            new_cells_to_check = set()
            # can optimize by only looking at cells or neighbors that have changed
            for coords in self.cells_to_check:
                try:
                    cell = self.get_cell(coords[0], coords[1])
                except (IndexError, KeyError, TypeError):
                    print(f"Invalid coordinates in set {coords}")
                    raise
                # returns true if modified
                if cell.live_or_die(self):
                    new_cells_to_check |= cell.get_coords_of_cell_and_neighbors(self)
            self.cells_to_check = new_cells_to_check
        else:
            # in case we haven't yet decided, check all cells
            self.cells_to_check = set()
            for col, column in enumerate(self.cell_grid):
                for row, cell in enumerate(column):
                    cell = cell if cell else Cell(col, row)
                    if cell.live_or_die(self):
                        self.cells_to_check |= cell.get_coords_of_cell_and_neighbors(self)
        # swap old grid for new
        self.set_grid()

    def set_grid(self) -> None:
        """ Fix generational changes """
        self.cell_grid = deepcopy(self.next_cell_grid)

    # helper private methods including error handling

    def __update_binary_grid(self, col: int, row: int, val: int) -> None:
        try:
            self.binary_grid[col][row] = val
        except IndexError:
            print(f"Tried to update {col} {row} outside of grid size {self.size}")
            raise

    def __init_next_gen(self, col: int, row: int) -> None:
        try:
            if not self.next_cell_grid[col][row]:
                self.next_cell_grid[col][row] = Cell(col, row)
        except IndexError:
            print(f"Tried to update cell {col} {row} outside of grid size {self.size}")
            raise

    def __kill_next_gen(self, col: int, row: int) -> None:
        self.__init_next_gen(col, row)
        try:
            self.next_cell_grid[col][row].kill()
        except IndexError:
            print(f"Tried to kill cell {col} {row} outside of grid size {self.size}")
            raise

    def __revive_next_gen(self, col: int, row: int) -> None:
        self.__init_next_gen(col, row)
        try:
            self.next_cell_grid[col][row].make_alive()
        except IndexError:
            print(f"Tried to revive cell {col} {row} outside of grid size {self.size}")
            raise
