import pygame
from src.map import Map

class Player:
    def __init__(self, lable):
        self.turn = True
        self.lable = lable
        self.__win = False
        
    def update(self, mouse_pos, map: Map):
        if self.turn:
            if pygame.mouse.get_pressed()[0]:
                i, j = map.getPositonSquare(mouse_pos)
                map.map[i][j].lable = self.lable
                if self.checkWin(i, j, map):
                    self.__win = True
                    
    
    def checkWin(self, i, j, map: Map):
        if self.checkRow(i, j, map) or self.checkCol(i, j, map) or self.checkDiagonalLine1(i, j, map) or self.checkDiagonalLine2(i, j, map):
            return True
        return False
        
    def checkRow(self, i, j, map: Map):
        d = 0 
        k = i 
        h = 0
        # check row
        while map.map[k][j].lable == map.map[i][j].lable:
            d += 1
            k += 1
        k = i - 1;
        while map.map[k][j].lable == map.map[i][j].lable:
            d += 1
            k -= 1
        return True if d > 4 else False
        
    def checkCol(self, i, j, map: Map):
        d = 0
        h = j
        while map.map[i][h].lable == map.map[i][j].lable:
            d += 1
            h += 1
        h = j - 1
        while  map.map[i][h].lable == map.map[i][j].lable:
            d += 1
            h -= 1
        return True if d > 4 else False

    def checkDiagonalLine1(self, i, j, map: Map):
        d = 0
        h = i
        k = j
        while map.map[h][k].lable == map.map[i][j].lable:
            h += 1
            k += 1
            d += 1
        h = i - 1
        k = j - 1
        while map.map[h][k].lable == map.map[i][j].lable:
            h -= 1
            k -= 1
            d += 1
        return True if d > 4 else False
    
    def checkDiagonalLine2(self, i, j, map: Map):
        d = 0
        h = i
        k = j
        while map.map[h][k].lable == map.map[i][j].lable:
            h += 1
            k -= 1
            d += 1
        h = i - 1
        k = j + 1
        while map.map[h][k].lable == map.map[i][j].lable:
            h -= 1
            k += 1
            d += 1
        return True if d > 4 else False
    
    def is_winner(self):
        return self.__win
    
    