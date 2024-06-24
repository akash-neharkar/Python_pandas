# 2878. Get the Size of a DataFrame
# Solved
# Easy
# Companies
# Hint
# DataFrame players:
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | player_id   | int    |
# | name        | object |
# | age         | int    |
# | position    | object |
# | ...         | ...    |
# +-------------+--------+
# Write a solution to calculate and display the number of rows and columns of players.

# Return the result as an array:

# [number of rows, number of columns]

# The result format is in the following example.


import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rows = len(players.axes[0])
    cols = len(players.axes[1])
    return [rows, cols]
    