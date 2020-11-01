import config_with_yaml as config

from views import grid

def main():
    cfg = config.load("config.yaml")

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

    print(f"Initilizing grid of size {grid_size} with {initial_cells} cells", grid_size, initial_cells)
    grid.show_grid(grid_size, initial_cells, rounds,
        seconds_between_rounds, random, min_neighbor_cells,
        max_neighbor_cells, cells_to_revive)

if __name__ == "__main__":
    main()
