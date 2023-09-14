import pygame
from src.map import Map
from src.lable import Lable
from src.check_win_able import CheckWinable

class Player(CheckWinable):
    count = 0
    def __init__(self, lable: Lable):
        CheckWinable.__init__(self)
        self.lable = lable
        
    def update(self, mouse_pos, matrix: Map): 
        try:
            i, j = matrix.getPositonSquare(mouse_pos)
            if matrix.matrix_square[i][j].is_empty:
                matrix.matrix_square[i][j].is_empty = False
                matrix.matrix_square[i][j].lable = self.lable
                Player.count += 1
                self.checking(i, j, matrix)
        except:...
    
    