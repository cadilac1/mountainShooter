import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.MENU2 import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT


class Game:

    def __init__(self):
        self.window = None
        pygame.init()
        window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

        def run(self, ):
            print("setup start")
            print("setup end")

        print("loop start")
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

