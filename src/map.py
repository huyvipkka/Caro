import pygame
from src.square import Square

class Map:
    map_size = (45, 25) #width, height
    square_size = 25
    map_size_px = (square_size*map_size[0]+1, square_size*map_size[1]+1)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.surface = pygame.Surface(Map.map_size_px)
        self.matrix_square = []
        for row in range(Map.map_size[1]):
            widths = []
            for col in range(Map.map_size[0]):
                new_square = Square(col*Map.square_size, row*Map.square_size, Map.square_size)
                widths.append(new_square)
            self.matrix_square.append(widths)
    
    def getPositonSquare(self, mouse_pos):
        mouse_pos = (mouse_pos[0] - self.x, mouse_pos[1] - self.y)
        for row_idx, row in enumerate(self.matrix_square):
            for square in row:
                if square.rect.collidepoint(mouse_pos):
                    col_idx = row.index(square)
                    return (row_idx, col_idx)
    
    def draw(self, screen, mouse_pos):
        mouse_pos = (mouse_pos[0] - self.x, mouse_pos[1] - self.y)
        self.surface.fill('white smoke')
        for i in range(Map.map_size[0]+1):
            pygame.draw.line(self.surface, 'black', (i*Map.square_size, 0), (i*Map.square_size, Map.map_size[1]*Map.square_size))
        for i in range(Map.map_size[1]+1):
            pygame.draw.line(self.surface, 'black', (0, i*Map.square_size), (Map.map_size[0]*Map.square_size, i*Map.square_size))
        for row in self.matrix_square:
            for square in row:
                square.draw(self.surface, mouse_pos)
        screen.blit(self.surface, (self.x, self.y))