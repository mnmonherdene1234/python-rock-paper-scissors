import pygame
import sys
import scenes.scene_manager as sm
from scenes.game_scene import GameScene

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Rock, Paper, Scissors Game")

running = True
sm.screen = screen
sm.scene = GameScene(screen)

while running:
    for event in pygame.event.get():
        sm.event(event)
        if event.type == pygame.QUIT:
            running = False

    sm.update()
    pygame.display.update()

pygame.quit()
sys.exit()
