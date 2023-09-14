from src.player import Player
from src.map import Map
import random


class Bot(Player):
    def __init__(self, lable):
        Player.__init__(self, lable)
        
    def update(self, caro_map: Map):
        while True:
            i = random.randint(0, Map.map_size[1]-1)
            j = random.randint(0, Map.map_size[0]-1)
            if caro_map.matrix_square[i][j].is_empty == True:
                break
        caro_map.matrix_square[i][j].lable = self.lable
        caro_map.matrix_square[i][j].is_empty = False
        Player.count += 1
        self.checking(i, j, caro_map)