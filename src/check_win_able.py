from src.map import Map

class CheckWinable:
    def checkWin(self, i, j, map: Map):
        if self.__checkRow(i, j, map) or self.__checkCol(i, j, map) or self.__checkDiagonalLine1(i, j, map) or self.__checkDiagonalLine2(i, j, map):
            return True
        return False
        
    def __checkRow(self, i, j, map: Map):
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
        
    def __checkCol(self, i, j, map: Map):
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

    def __checkDiagonalLine1(self, i, j, map: Map):
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
    
    def __checkDiagonalLine2(self, i, j, map: Map):
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