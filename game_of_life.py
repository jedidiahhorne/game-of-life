"""
Game of life implements Conway's Game of Life.
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
Usage:
python3 game_of_life.py:
"""

import config_with_yaml as config

from views import grid

def main():
    """
    Get configs and invoke view.
    """
    cfg = config.load("config.yaml")
    size = cfg.getProperty("grid.size")
    cells = cfg.getProperty("grid.initial_cells")
    print(f"Initializing grid of size {size} with {cells} cells")
    grid.show_grid(cfg)

if __name__ == "__main__":
    main()
