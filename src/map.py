import pygame
from src.square import Square

class Map:
    map_size = (30, 20) #width, height
    square_size = 30
    def __init__(self):
        self.map = []
        for row in range(Map.map_size[1]):
            widths = []
            for col in range(Map.map_size[0]):
                new_square = Square(col*Map.square_size, row*Map.square_size, Map.square_size)
                widths.append(new_square)
            self.map.append(widths)
                
    def update(self): ...
    
    def getSquare(self, mouse_pos):
        for row in self.map:
            for square in row:
                if square.rect.collidepoint(mouse_pos):
                    return square
        return False
    
    def getPositonSquare(self, mouse_pos):
        for row_idx, row in enumerate(self.map):
            for square in row:
                if square.rect.collidepoint(mouse_pos):
                    col_idx = row.index(square)
                    return (row_idx, col_idx)
    
    def draw(self, screen):
        for row in self.map:
            for square in row:
                square.draw(screen)