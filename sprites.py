import pygame
from settings import *

class Background(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        bg_img = pygame.image.load("imgs/bg.png").convert()

        self.image = pygame.transform.scale(bg_img, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.pos = pygame.math.Vector2(self.rect.topleft)
    
    def update(self, dt):
        pass


class Ground(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        ground_surf = pygame.image.load("imgs/base.png").convert()

        self.image = pygame.transform.scale(ground_surf, (WINDOW_WIDTH, ground_surf.get_height()))
        self.rect = self.image.get_rect(bottomleft=(0, WINDOW_HEIGHT))
        self.pos = pygame.math.Vector2(self.rect.bottomright)
