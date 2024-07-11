import pygame
pygame.init()

size = width, height = 280, 512
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
x, y = 140, 256

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("green")
    if clock.get_time() % 2 == 0:
        x -= 8
        x %= width

    pygame.draw.rect(screen, "blue", pygame.Rect((x + 50, y - 300), (45, 200)))
    pygame.draw.rect(screen, "blue", pygame.Rect((x + 50, y + 100), (45, 200)))
    pygame.draw.circle(screen, "red", (width // 2, height // 2), 30)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
