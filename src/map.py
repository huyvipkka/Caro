import pygame
from src.square import Square

class Map:
    map_size = (30, 25) #width, height
    square_size = 25
    def __init__(self):
        self.matrix_square = []
        for row in range(Map.map_size[1]):
            widths = []
            for col in range(Map.map_size[0]):
                new_square = Square(col*Map.square_size, row*Map.square_size, Map.square_size)
                widths.append(new_square)
            self.matrix_square.append(widths)
                
    def update(self): ...
    
    def getSquare(self, mouse_pos):
        for row in self.matrix_square:
            for square in row:
                if square.rect.collidepoint(mouse_pos):
                    return square
    
    def getPositonSquare(self, mouse_pos):
        for row_idx, row in enumerate(self.matrix_square):
            for square in row:
                if square.rect.collidepoint(mouse_pos):
                    col_idx = row.index(square)
                    return (row_idx, col_idx)
    
    def draw(self, screen, mouse_pos):
        for i in range(Map.map_size[0]+1):
            pygame.draw.line(screen, 'black', (i*Map.square_size, 0), (i*Map.square_size, Map.map_size[1]*Map.square_size))
        for i in range(Map.map_size[1]+1):
            pygame.draw.line(screen, 'black', (0, i*Map.square_size), (Map.map_size[0]*Map.square_size, i*Map.square_size))
        for row in self.matrix_square:
            for square in row:
                square.draw(screen, mouse_pos)