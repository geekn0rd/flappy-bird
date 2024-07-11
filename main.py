import pygame
import sys
import time

from settings import *
from sprites import Background, Ground, Bird

class Game():
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Flappy Bird!")
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.bg = Background(self.all_sprites)
        self.gound = Ground(self.all_sprites)
        self.bird = Bird(self.all_sprites, scale_factor=1.5)
    
    def run(self):
        last_time = time.time()
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    self.bird.jump()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            dt = time.time() - last_time
            last_time = time.time() 
            
            # Game logic
            self.display.fill("black")
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display)

            pygame.display.update()
            self.clock.tick(FPS)

    
if __name__ == "__main__":
    game = Game()
    game.run()
