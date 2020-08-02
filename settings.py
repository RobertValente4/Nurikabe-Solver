# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:52:04 2020

@author: rvale
"""
# Following along with A Plus Coding on youtube for this part.

WIDTH = 600
HEIGHT = 600

# Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTGREY = (215,215,215)
GREY = (128,128,128)

# Boards
testBoard1 = [[0 for x in range(9)] for x in range(9)]

testBoard2 = [[0,1,0,0,4,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [6,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,1,0,0,0],
              [1,0,0,0,0,0,0,0,8],
              [0,0,0,4,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,8],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,5,0,0,1,0]]

# Postitions and Sizes
gridPos = (75,100)
cellSize = 50
gridSize = cellSize*9