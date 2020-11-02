"""
Cell contains logic for game.
A live cell can be killed by underpopulation or overpopulation of neighbors (configurable).
A dead cell can be revived by reproduction of neighbors.
"""


class Cell:
    """ A cell """

    def __init__(self, col: int, row: int):
        self.alive = False
        self.row = row
        self.col = col

    def kill(self):
        """ Kill """
        self.alive = False

    def make_alive(self):
        """ Revive """
        self.alive = True

    def is_alive(self):
        """ Is alive """
        return self.alive

    def live_or_die(self, board) -> bool:
        """ Logic for whether cell should be killed or revived based on neighbors. """
        is_modified = False
        neighbor_count = 0
        for cell in self.__get_neighbors(board):
            if cell.is_alive():
                neighbor_count += 1
        # alive cells can be killed
        if self.is_alive():
            if (neighbor_count > board.game_config["max_live"] or
                    neighbor_count < board.game_config["min_live"]):
                print(f"Killing cell {self.col} {self.row} neighbors {neighbor_count}")
                is_modified = True
                board.kill(self.col, self.row)
        # dead cells can be revived
        else:
            if neighbor_count == board.game_config["revive"]:
                print(f"Reviving cell {self.col} {self.row} neighbors {neighbor_count}")
                is_modified = True
                board.make_alive(self.col, self.row)
        return is_modified

    def get_coords_of_cell_and_neighbors(self, board) -> set:
        """ Get coords to determine cells to update on board. """
        coords = set()
        coords.add((self.col, self.row))
        for cell in self.__get_neighbors(board):
            coords.add((cell.col, cell.row))
        return coords

    def __get_neighbors(self, board):
        shifts = (-1, 0, 1)
        center_x = self.col
        center_y = self.row
        for col in shifts:
            neighbor_x = center_x + col
            # boundary conditions - wrap
            if neighbor_x < 0:
                neighbor_x = board.size - 1
            if neighbor_x > board.size - 1:
                neighbor_x = 0
            for row in shifts:
                neighbor_y = center_y + row
                if neighbor_y < 0:
                    neighbor_y = board.size - 1
                if neighbor_y > board.size - 1:
                    neighbor_y = 0
                # ignore center cell itself
                if col != 0 or row != 0:
                    yield board.get_cell(neighbor_x, neighbor_y)
