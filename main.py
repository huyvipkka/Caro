import pygame
from src.lable import Lable
from src.player import Player
from src.map import Map

pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
FPS = 60
running = True

x = Lable('x', 'red')
o = Lable('o', 'green')
caro_map = Map()
player1 = Player(x)
player2 = Player(o)

while running:
    screen.fill("black")
    
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                print(player1.count)
                if player1.count % 2 == 0:
                    player1.update(mouse_pos, caro_map)
                    if player1.is_winner():
                        print('player 1 win')
                else:
                    player2.update(mouse_pos, caro_map)
                    if player2.is_winner():
                        print('player 2 win')

    caro_map.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()