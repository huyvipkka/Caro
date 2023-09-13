import pygame
from src.map import Map

class CheckWinable:
    def __init__(self):
        self.__row = False
        self.__col = False
        self.__diagonal_line1 = False
        self.__diagonal_line2 = False
        self.start_pos = ()
        self.end_pos = ()
    
    def checking(self, i, j, caro_map: Map):
        
        self.__checkCol(i, j, caro_map)
        self.__checkRow(i, j, caro_map)
        self.__checkDiagonalLine1(i, j, caro_map)
        self.__checkDiagonalLine2(i, j, caro_map)
    
    def checkWin(self) -> bool:
        if self.__col or self.__row or self.__diagonal_line1 or self.__diagonal_line2:
            return True
        return False
        
    def drawWinLine(self, screen, caro_map: Map, color):
        if self.__row or self.__col or self.__diagonal_line1 or self.__diagonal_line2:
            pygame.draw.line(screen, color, self.start_pos, self.end_pos, 3)
        
    
    def __checkRow(self, i, j, caro_map: Map):
        d = 0 
        endx = j
        while caro_map.matrix_square[i][endx].lable == caro_map.matrix_square[i][j].lable and endx < Map.map_size[0]-1:
            d += 1
            endx += 1
        endx -= 1
        startx = j - 1
        while caro_map.matrix_square[i][startx].lable == caro_map.matrix_square[i][j].lable and startx > 0:
            d += 1
            startx -= 1
        startx += 1
        if d > 4:
            self.start_pos = (caro_map.matrix_square[i][startx].rect.left,
                              caro_map.matrix_square[i][startx].rect.centery)
            self.end_pos = (caro_map.matrix_square[i][endx].rect.right,
                              caro_map.matrix_square[i][endx].rect.centery)
            self.__row = True
        
    def __checkCol(self, i, j, caro_map: Map):
        d = 0 
        endy = i
        while caro_map.matrix_square[endy][j].lable == caro_map.matrix_square[i][j].lable and endy < Map.map_size[1]-1:
            d += 1
            endy += 1
        endy -= 1
        starty = i - 1
        while caro_map.matrix_square[starty][j].lable == caro_map.matrix_square[i][j].lable and starty > 0:
            d += 1
            starty -= 1
        starty += 1
        if d > 4:
            self.start_pos = (caro_map.matrix_square[starty][j].rect.centerx, 
                              caro_map.matrix_square[starty][j].rect.top,)
            self.end_pos = (caro_map.matrix_square[endy][j].rect.centerx,
                            caro_map.matrix_square[endy][j].rect.bottom)
            self.__row = True

    def __checkDiagonalLine1(self, i, j, caro_map: Map):
        d = 0
        endy = i
        endx = j
        while caro_map.matrix_square[endy][endx].lable == caro_map.matrix_square[i][j].lable and endx < Map.map_size[0]-1 and endy < Map.map_size[1]:
            endy += 1
            endx += 1
            d += 1
        endx -= 1
        endy -= 1
        startx = j - 1
        starty = i - 1
        while caro_map.matrix_square[starty][startx].lable == caro_map.matrix_square[i][j].lable and startx > 0 and starty > 0:
            startx -= 1
            starty -= 1
            d += 1
        startx += 1
        starty += 1
        if d > 4:
            self.__diagonal_line1 = True
            self.start_pos = caro_map.matrix_square[starty][startx].rect.topleft
            self.end_pos = caro_map.matrix_square[endy][endx].rect.bottomright
             
    def __checkDiagonalLine2(self, i, j, caro_map: Map):
        d = 0
        endy = i
        endx = j
        while caro_map.matrix_square[endy][endx].lable == caro_map.matrix_square[i][j].lable and endx > 0 and endy < Map.map_size[1]-1:
            endy += 1
            endx -= 1
            d += 1
        endx += 1
        endy -= 1
        startx = j + 1
        starty = i - 1
        while caro_map.matrix_square[starty][startx].lable == caro_map.matrix_square[i][j].lable and startx < Map.map_size[0]-1 and starty > 0:
            startx += 1
            starty -= 1
            d += 1
        startx -= 1
        starty += 1
        if d > 4:
            self.__diagonal_line1 = True
            self.start_pos = caro_map.matrix_square[starty][startx].rect.topright
            self.end_pos = caro_map.matrix_square[endy][endx].rect.bottomleft