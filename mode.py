import pygame
from src.lable import Lable
from src.player import Player
from src.map import Map

screen = pygame.display.set_mode((1000, 626))
clock = pygame.time.Clock()

def Game2Player():
    FPS = 60
    running = True

    x = Lable('x', 'red')
    o = Lable('o', 'green')
    caro_map = Map()
    player1 = Player(x)
    player2 = Player(o)

    while running:
        screen.fill("white")
        
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    try:
                        i, j = caro_map.getPositonSquare(mouse_pos)
                        if Player.count % 2 == 0:
                            player1.update(mouse_pos, i, j, caro_map)
                        else:
                            player2.update(mouse_pos, i, j, caro_map)
                    except:...
                        
                        
        caro_map.draw(screen, mouse_pos)
        if player1.checkWin():
            player1.drawWinLine(screen, caro_map, player1.lable.color)
        elif player2.checkWin():
            player2.drawWinLine(screen, caro_map, player2.lable.color)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()