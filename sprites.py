import pygame
from random import choice, randint
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
        self.pos = pygame.math.Vector2(self.rect.topleft)
    
    def update(self, dt):
        pass


class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups, scale_factor=1.0):
        super().__init__(*groups)

        self.import_frames(scale_factor)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

        self.rect = self.image.get_rect(midleft=(WINDOW_WIDTH / 20, WINDOW_HEIGHT / 2))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        self.gravity = 1000
        self.direction = 0

    def import_frames(self, scale_factor):
        self.frames = []
        for i in range(1, 4):
            surf = pygame.image.load(f"imgs/bird{i}.png").convert_alpha()
            scaled_surf = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)
            self.frames.append(scaled_surf)
    
    def affect_gravity(self, dt):
        self.direction += self.gravity * dt
        self.pos.y += self.direction * dt 
        self.rect.y = round(self.pos.y)
    
    def jump(self):
        self.direction = -400

    def animate(self, dt):
        self.frame_index += 10 * dt
        self.frame_index %= 3
        self.image = self.frames[int(self.frame_index)]

    def rotate(self):
        rotated_bird = pygame.transform.rotozoom(self.image, 0.06 * -self.direction, 1)
        self.image = rotated_bird

    def update(self, dt):
        self.affect_gravity(dt)
        self.animate(dt)
        self.rotate()
        pass


class Pipe(pygame.sprite.Sprite):
    def __init__(self, *groups, scale_factor=1.0):
        super().__init__(*groups)

        orientation = choice(("up", "down"))

        surf = pygame.image.load("imgs/pipe.png").convert_alpha()
        scaled_surf = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)
        self.image = scaled_surf

        x = WINDOW_WIDTH + randint(40, 100)
        if orientation == "down":
            y = WINDOW_HEIGHT + randint(10, 50)
            self.rect = self.image.get_rect(midbottom=(x, y))
        else:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(midtop=(x, randint(-50, -10)))
        
        self.pos = pygame.math.Vector2(self.rect.topleft)
    
    def update(self, dt):
        self.pos.x -= 400 * dt
        self.rect.x = round(self.pos.x)
        if self.rect.right <= -100:
            self.kill()


       
