#!/usr/bin/env python

import random
import subprocess

PLUS = chr(206)
PIPE = chr(186)
BAR = chr(205)
PLUS = '+'
PIPE = '|'
BAR = '-'

def make_maze(width=10, height=10, random_maze=False):
    maze = []
    for i in range(width):
        column = []
        maze.append(column)
        for j in range(height):
            if random_maze:
                top = random.randrange(0,2) == 0
                right = random.randrange(0,2) == 0
                bottom = random.randrange(0,2) == 0
                left = random.randrange(0,2) == 0
                visited = random.randrange(0,2) == 0
                newNode = (top, right, bottom, left, visited)
            else:
                # top, right, bottom, left, visited flags
                newNode = (False, False, False, False, False)
            column.append(newNode)
    return maze


def carve_maze(maze):
    pass

def show_maze(maze, show_visited=False, current=None):
    subprocess.call('clear')
    for row in maze:
        # for each row, print two lines
        # first line is +-+- ...
        line1 = []
        for node in row:
            line1.append(PLUS)
            if node[0]:
                line1.append(' ')
            else:
                line1.append(BAR)
        line1.append(PLUS)
        # line 2 is | | |
        line2 = []
        for node in row:
            if node[3]:
                line2.append(' ')
            else:
                line2.append(PIPE)
            if show_visited and node[4]:
                line2.append('.')
            else:
                line2.append(' ')
        if row[-1][1]:
            line2.append(' ')
        else:
            line2.append(PIPE)
        print ''.join(line1)
        print ''.join(line2)
    lastline = []
    for node in maze[-1]:
        lastline.append(PLUS)
        if node[2]:
            lastline.append(' ')
        else:
            lastline.append(BAR)
    lastline.append(PLUS)
    print ''.join(lastline)

if __name__ == "__main__":
    maze = make_maze(random_maze=True)
    show_maze(maze)

