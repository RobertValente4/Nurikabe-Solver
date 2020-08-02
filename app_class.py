# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 18:16:03 2020

@author: rvale
"""

# From A Plus Coding's sudoku video

import pygame, sys
from settings import *
from button_class import *

class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        self.running = True
        self.grid = testBoard2
        pygame.display.set_caption('Nurikabe Solver V1')
        self.selected = None
        self.mousePos = None
        self.state = "playing"
        self.playing_Buttons = []
        self.menu_Buttons = []
        self.end_Buttons = []
        self.lockedCells = []
        self.font = pygame.font.SysFont("Century", cellSize)
        self.load()
        
    def run(self):
        while self.running:
            if self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
        pygame.quit()
        sys.exit()
        
### PLAYING STATE FUNCTIONS ###        
        
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.mouseOnGrid():
                    num = self.grid[self.selected[1]][self.selected[0]]
                    if num == 0:
                        self.grid[self.selected[1]][self.selected[0]] = -1
                    elif num == -1:
                        self.grid[self.selected[1]][self.selected[0]] = -2
                    elif num == -2:
                        self.grid[self.selected[1]][self.selected[0]] = 0
    
    def playing_update(self):
        self.mousePos = pygame.mouse.get_pos()
        selected = self.mouseOnGrid()
        if selected:
            self.selected = selected
        else:
            self.selected = None
         
        '''    
        for button in self.playing_Buttons:
            button.update(self.mousePos)
        '''
    def playing_draw(self):
        
        self.window.fill(WHITE)
        
        for button in self.playing_Buttons:
            button.draw(self.window)
            
        if self.selected:
            self.drawSelection(self.window, self.selected)
            
        self.shadeLockedCells(self.window,self.lockedCells)
        
        self.drawNumbers(self.window)
        
        self.drawGrid(self.window)
        pygame.display.update()
        
### HELPER FUNCTIONS ###     
        
    def shadeLockedCells(self,window,locked):
        for cell in locked:
            pygame.draw.rect(window, WHITE, (cell[0]*cellSize+gridPos[0], cell[1]*cellSize+gridPos[1], cellSize, cellSize))
    
    def drawNumbers(self, window):
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num > 0:
                    pos = [xidx*cellSize + gridPos[0], yidx*cellSize + gridPos[1]]
                    self.textToScreen(window, str(num), pos)
                if num == -1:
                    pygame.draw.rect(window, BLACK, (xidx*cellSize+gridPos[0], yidx*cellSize+gridPos[1], cellSize, cellSize))
                if num == -2:
                    pygame.draw.circle(window, BLACK, (xidx*cellSize+gridPos[0] + cellSize//2 + 1, yidx*cellSize+gridPos[1] + cellSize//2 + 1), cellSize//6)
        
    def drawSelection(self, window, pos):
        pygame.draw.rect(window, LIGHTGREY, (pos[0]*cellSize+gridPos[0], pos[1]*cellSize+gridPos[1], cellSize, cellSize))
        
    def drawGrid(self, window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH-150, HEIGHT-150),2)
        for x in range(9):
            pygame.draw.line(window, BLACK, (gridPos[0]+(x*cellSize), gridPos[1]), (gridPos[0]+(x*cellSize), gridPos[1]+450),2)
            pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1]+(x*cellSize)), (gridPos[0]+450,gridPos[1]+(x*cellSize)),2)
            
    def mouseOnGrid(self):
        if self.mousePos[0] < gridPos[0] or self.mousePos[1] < gridPos[1]:
            return False
        if self.mousePos[0] > gridPos[0] + gridSize or self.mousePos[1] > gridPos[1] + gridSize:
            return False
        return ((self.mousePos[0] - gridPos[0])//cellSize, (self.mousePos[1] - gridPos[1])//cellSize)
            
    def loadButtons(self):
        self.playing_Buttons.append(Button(20,40,100,40,"Button",GREY,LIGHTGREY,None,None))
        
    def textToScreen(self, window, text, pos):
        font = self.font.render(text,False,BLACK)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (cellSize - fontWidth)//2
        pos[1] += (cellSize - fontHeight)//2
        window.blit(font,pos)
        
    def load(self):
      #  self.loadButtons()
        
        # Set locked cells
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num > 0:
                    self.lockedCells.append([xidx,yidx])