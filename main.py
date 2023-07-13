import pygame
import sys
import scenes.scenes_manager as sm
from assets.images import game_icon
from scenes.game_scene import GameScene

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Rock, Paper, Scissors Game")
pygame.display.set_icon(game_icon)

sm.screen = screen
sm.scene = GameScene(screen)

while sm.running:
    sm.update()
    pygame.display.flip()

pygame.quit()
sys.exit()
