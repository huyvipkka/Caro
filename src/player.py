import pygame
from src.map import Map
from src.lable import Lable
from src.check_win_able import CheckWinable

class Player(CheckWinable):
    count = 0
    def __init__(self, lable: Lable):
        CheckWinable.__init__(self)
        self.lable = lable
        self.__win = False
        
    def update(self, mouse_pos, i, j, matrix: Map):
        if matrix.matrix_square[i][j].is_empty:
            matrix.matrix_square[i][j].is_empty = False
            matrix.matrix_square[i][j].lable = self.lable
            Player.count += 1
            self.checking(i, j, matrix)
            if self.checkWin():
                self.__win = True

    
    