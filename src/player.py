import pygame
from src.map import Map
from src.lable import Lable
from src.check_win_able import CheckWinable

class Player(CheckWinable):
    def __init__(self, lable: Lable):
        CheckWinable.__init__(self)
        self.lable = lable
        self.__win = False
    
    count = 0
    def update(self, mouse_pos, map: Map):
        try:
            i, j = map.getPositonSquare(mouse_pos)
            if map.map[i][j].is_able:
                map.map[i][j].lable = self.lable
                map.map[i][j].is_able = False
                Player.count += 1
                if self.checkWin(i, j, map):
                    self.__win = True
        except:
            ...

    
    def is_winner(self):
        return self.__win
    
    