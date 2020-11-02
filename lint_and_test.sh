#!/bin/bash

# lint
pylint game_of_life.py
pylint models
pylint views
pylint tests

# test
coverage run -m pytest
coverage report -m ./models/*.py
coverage report -m ./views/*.py
