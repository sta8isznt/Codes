import pygame as pg
import sys
import time
import random

from settings import Settings
from ship import Ship

class Alien_Invasion:
    def __init__(self):
        pg.init()
        self.backround_image = pg.image.load("images/space_image.jpg")

        # settings
        self.settings = Settings()


        # screen settings
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption("speis inveiderz")

        #Clock Settings
        self.clock = pg.time.Clock()

        # Ship
        self.ship = Ship(self)

    def run(self):
        """Runs the Game"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            

    def _check_events(self):
        """Chech for new events"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """Updates the screen"""
        self.screen.blit(self.backround_image, (0, 0))

        self.ship.blitme()
        pg.display.update()

    def _check_keydown_events(self, event):
        pass

    def _check_keyup_events(self, event):
        pass










my_game = Alien_Invasion()
my_game.run()
