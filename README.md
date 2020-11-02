# game-of-life
Conway's Game of Life

```
virtualenv --python=python3.8 env
source env/bin/activate
pip3 install -r requirements.txt
# lint
sh lint.sh
# run
python3 game_of_life.py
python3 -m pytest
```