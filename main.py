import pygame
import sys
from images import background_image, rock_button, paper_button, scissors_button

pygame.init()

screen = pygame.display.set_mode((600, 600))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(background_image, (0, 0))
    screen.blit(rock_button, (100, 500))
    screen.blit(paper_button, (200, 500))
    screen.blit(scissors_button, (300, 500))
    pygame.display.flip()

pygame.quit()
sys.exit()
