import pygame
import sys
import time

from settings import *

class Game():
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Flappy Bird!")
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
    
    def run(self):
        last_time = time.time()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            dt = time.time() - last_time
            last_time = time.time() 
            
            pygame.display.update()
            self.clock.tick(FPS)

    

if __name__ == "__main__":
    game = Game()
    game.run()
