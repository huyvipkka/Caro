import pygame
from src.lable import Lable
from src.player import Player
from src.map import Map
from src.bot import Bot
from src.button import Button

scr_width = 1000
scr_height = 626
screen = pygame.display.set_mode((scr_width, scr_height))
clock = pygame.time.Clock()
FPS = 60
font_big = pygame.font.SysFont("Lucida Sans", 35)

def Start():
    running = True
    
    while running:
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        game_1_plater_btn = Button("1 Player", font_big, 'black', 'AQUA', pygame.Rect(scr_width//2-70, 175, 140, 50))
        game_2_plater_btn = Button("2 Player", font_big, 'black', 'AQUA', pygame.Rect(scr_width//2-70, 275, 140, 50))
        quit_btn = Button("Quit", font_big, 'black', 'AQUA', pygame.Rect(scr_width//2-70, 375, 140, 50))
        game_1_plater_btn.draw(screen)
        game_2_plater_btn.draw(screen)
        quit_btn.draw(screen)
        if game_1_plater_btn.check():
            Game1Player()
        if game_2_plater_btn.check():
            Game2Player()
        if quit_btn.check():
            running = False
            
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    
def EndGame(winner):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.draw.rect(screen, 'gray', (scr_width*0.3, scr_height*0.15, scr_width*0.4, scr_height*0.7), 0, 10)
        pygame.draw.rect(screen, 'black', (scr_width*0.3, scr_height*0.15, scr_width*0.4, scr_height*0.7), 10, 10)
        
        text = winner + ' win'
        size_text = pygame.font.Font.size(font_big, text)
        DrawText(screen, text, 'black', font_big, (scr_width//2 - size_text[0]//2, scr_height*0.3))
        
        game_1_plater_btn = Button("1 Player", font_big, 'black', 'AQUA', pygame.Rect(scr_width//2-70, scr_height*0.4, 140, 50))
        game_2_plater_btn = Button("2 Player", font_big, 'black', 'AQUA', pygame.Rect(scr_width//2-70, scr_height*0.5, 140, 50))
        quit_btn = Button("Quit", font_big, 'black', 'AQUA', pygame.Rect(scr_width//2-70, scr_height*0.6, 140, 50))
        game_1_plater_btn.draw(screen)
        game_2_plater_btn.draw(screen)
        quit_btn.draw(screen)
        if game_1_plater_btn.check():
            Game1Player()
        if game_2_plater_btn.check():
            Game2Player()
        if quit_btn.check():
            running = False
        
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    
def Game2Player():
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
                    if Player.count % 2 == 0:
                        player1.update(mouse_pos, caro_map)
                    else:
                        player2.update(mouse_pos, caro_map)
        text = 'O turn'
        if Player.count % 2 == 0:
            text = 'X turn'
        DrawText(screen, text, 'black', font_big, (760, 10))
                        
        caro_map.draw(screen, mouse_pos)
        if player1.checkWin():
            player1.drawWinLine(screen, caro_map, player1.lable.color)
            EndGame(player1.lable.text)
        elif player2.checkWin():
            player2.drawWinLine(screen, caro_map, player2.lable.color)
            EndGame(player2.lable.text)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    
def Game1Player():
    running = True

    x = Lable('x', 'red')
    o = Lable('o', 'green')
    caro_map = Map()
    player1 = Player(x)
    bot = Bot(o)

    while running:
        screen.fill("white")
        
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if Player.count % 2 == 0:
                        player1.update(mouse_pos, caro_map)
        text = 'X turn'
        if Player.count % 2 != 0:
            bot.update(caro_map)
            text = 'O turn'
        DrawText(screen, text, 'black', font_big, (760, 10))
                                  
        caro_map.draw(screen, mouse_pos)
        if player1.checkWin():
            player1.drawWinLine(screen, caro_map, player1.lable.color)
            EndGame(player1.lable.text)
        elif bot.checkWin():
            bot.drawWinLine(screen, caro_map, bot.lable.color)
            EndGame(bot.lable.text)
            
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    
def DrawText(screen, text, color, font, position):
    render = font.render(text, True, color)
    screen.blit(render, position)