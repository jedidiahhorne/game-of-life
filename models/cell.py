class Cell:
    """ A cell """

    def __init__(self, x: int, y: int):
        self.alive = False
        self.x = x
        self.y = y

    def kill(self):
        self.alive = False

    def make_alive(self):
        self.alive = True

    def is_alive(self):
        return self.alive

    def live_or_die(self, board):
        neighbor_count = 0
        for cell in self.__get_neighbors(board):
            if cell.is_alive():
                # print(f"Neighbor at {cell.x} {cell.y} is alive")
                neighbor_count += 1
        if self.is_alive():
            if neighbor_count > board.max_neighbor_cells or neighbor_count < board.min_neighbor_cells:
               print(f"Killing cell {self.x} {self.y} neighbors {neighbor_count}") 
               board.kill(self.x, self.y)
        # dead
        else:
            if neighbor_count == board.cells_to_revive:
                print(f"Reviving cell {self.x} {self.y} neighbors {neighbor_count}")
                board.make_alive(self.x, self.y)
        # print(f"Cell {self.x} {self.y} neighbors {neighbor_count}")
        # print(f"Cell {self.x} {self.y} has {neighbor_count} live neighbors")

    def __get_neighbors(self, board):
        # use wrap-around method to avoid issues with boundaries
        shifts = (-1, 0, 1)
        center_x = self.x
        center_y = self.y
        for x in shifts:
            neighbor_x = center_x + x
            # boundary conditions - wrap
            if neighbor_x < 0:
                neighbor_x = board.size - 1
            if neighbor_x > board.size - 1:
                neighbor_x = 0
            for y in shifts:                
                neighbor_y = center_y + y
                if neighbor_y < 0:
                    neighbor_y = board.size - 1
                if neighbor_y > board.size -1:
                    neighbor_y = 0
                # ignore center cell itself
                if x != 0 or y != 0:
                    # print(f"Checking {neighbor_x} {neighbor_y}")
                    yield board.get_cell(neighbor_x, neighbor_y)

        def __float__(self):
            try:
                return 1.0 if self.is_alive else 0.0
            except ValueError:
                return None
