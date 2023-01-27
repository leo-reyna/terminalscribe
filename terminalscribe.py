# RL Jan 2023
# terminalscribe exercise


import os
import time
from termcolor import colored

os.system('cls')

class Canvas:
    def __init__(self, width, height) -> None:
        pass
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y) for x in range(self._x)]]
    def hitsWall(self,point):
        return point[0] < 0 or point[0] >= self._x or point[1]