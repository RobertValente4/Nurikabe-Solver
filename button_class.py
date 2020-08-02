# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 01:01:26 2020

@author: rvale
"""

import pygame

class Button:
    
    def __init__(self, x, y, width, height, text,colour, hlcolour, function, params):
        self.image = pygame.Surface((width,height))
        self.pos = (x,y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.text = text
        self.colour = colour
        self.hlcolour = hlcolour
        self.function = function
        self.params = params
        self.highlighted = False
        
    def update(self,mouse):
        if self.rect.collidepoint(mouse):
            self.highlighted = True
        else:
            self.highlighted = False
    
    def draw(self, window):
        self.image.fill(self.hlcolour if self.highlighted else self.colour)
        window.blit(self.image, self.pos)