import pygame
import sys
import time

from settings import *
from sprites import Background, Ground, Bird, Pipe

class Game():
    def __init__(self):
        # Game setup
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Flappy Bird!")
        self.clock = pygame.time.Clock()
        self.active = True
        self.start_offset = 0

        # Sprites
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.bg = Background(self.all_sprites)
        self.gound = Ground([self.all_sprites, self.collision_sprites])
        self.bird = Bird(self.all_sprites, scale_factor=1.5)

        # Timer
        self.pipe_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.pipe_timer, 1400)

        # Text
        self.font = pygame.font.SysFont('arial', 28, True)
        self.score = 0
    
    def collisions(self):
        if pygame.sprite.spritecollide(self.bird, self.collision_sprites, False, pygame.sprite.collide_mask)\
            or self.bird.rect.top <= 0:
            self.active = False
            for sprite in self.collision_sprites:
                if isinstance(sprite, Pipe):
                    sprite.kill()
            self.bird.kill()

    def display_score(self):
        if not self.active:
            return
        self.score = (pygame.time.get_ticks() - self.start_offset) // 200
        score_surf =  self.font.render(str(self.score), True, "white")
        score_rect = score_surf.get_rect(midtop=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 10))
        self.display.blit(score_surf, score_rect)
        
    def run(self):
        last_time = time.time()
        while True:
            # Event loop
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    if self.active:
                        self.bird.jump()
                    else:
                        self.active = True
                        self.start_offset = pygame.time.get_ticks()
                        self.bird = Bird(self.all_sprites, scale_factor=1.5)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == self.pipe_timer and self.active:
                    Pipe([self.all_sprites, self.collision_sprites], scale_factor=1.08)
            
            dt = time.time() - last_time
            last_time = time.time() 
            
            # Game logic
            self.display.fill("black")
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display)
            self.display_score()

            if self.active:
                self.collisions()
            else:
                go_surf =  pygame.font.SysFont('timesnewroman', 70, True).render("Game Over", True, (235, 58, 14))
                go_rect = go_surf.get_rect(midtop=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
                self.display.blit(go_surf, go_rect)

            pygame.display.update()
            self.clock.tick(FPS)

    
if __name__ == "__main__":
    game = Game()
    game.run()
