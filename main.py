import pygame
from src.player import Player
from src.map import Map

pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
FPS = 60
running = True

caro_map = Map()
player = Player('x')

while running:
    screen.fill("black")
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(mouse_pos, caro_map)
    if player.is_winner():
        print('win')

    caro_map.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()