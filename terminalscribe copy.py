import os
import time
import math
from termcolor import colored, cprint

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [['░' for y in range(self._y)] for x in range(self._x)] # '' = you can use whatever your want to draw the canvas

    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
           cprint(' '.join([col[y] for col in self._canvas]),"red")

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '•'
        self.mark = '▒'
        self.framerate = 0.5 # was 0.2
        self.pos = [2, 2] # was 0, 0 

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, "green"))
        self.canvas.print()
        time.sleep(self.framerate)

    def drawCircle(self, center, radius):
        for theta in range(0, 360, 5):
            x = center[0] + radius * math.cos(math.radians(theta))
            y = center[1] + radius * math.sin(math.radians(theta))
            pos = [int(x), int(y)]
            self.draw(pos)

canvas = Canvas(14, 9) # 14 columns #9 rows
scribe = TerminalScribe(canvas)

# Draw a circle with a center of [6, 4] and a radius of 3
scribe.drawCircle([6,4])
radius = 4
scribe.draw_circle(center, radius)
