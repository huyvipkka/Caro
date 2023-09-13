import pygame

pygame.init()
class Square:
    font_small = pygame.font.SysFont("Lucida Sans", 25)
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.__size = size
        self.lable = ''
        
    #draw square, centered lable and draw lable
    def draw(self, screen):
        pygame.draw.rect(screen, 'white', self.rect, 1)
        if self.lable != '':
            render = Square.font_small.render(self.lable, True, 'white')
            rect_render = (render.get_rect()[2], render.get_rect()[3])
            x = self.rect.left + (self.__size//2 - rect_render[0]//2)
            y = self.rect.top + (self.__size//2 - rect_render[1]//2)
            screen.blit(render, (x, y))