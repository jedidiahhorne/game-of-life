# game-of-life
Conway's Game of Life

```
virtualenv --python=python3.8 env
source env/bin/activate
pip3 install -r requirements.txt
# lint and test
sh lint_and_test.sh
# run
python3 game_of_life.py
```

Configuration

```
In the file config.yaml, you'll see different parameters to control the game.

You can set:

-- grid size (square)
-- number of initial cells
-- whether you randomly place cells initially or draw them via the interactive grid ("random")
-- time between rounds

Other advanced options include parameters of the game itself (number of adjacent cells to determine whether a cell lives or dies).

If you adjust the parameters you will need to end and restart the game to see the impact.

For more information see:

https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

``` 