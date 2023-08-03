import asyncio
import pygame
import sys
import scenes.scenes_manager as sm
from assets.images import game_icon


async def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Rock, Paper, Scissors Game")
    pygame.display.set_icon(game_icon)

    sm.init(screen)

    while sm.running:
        sm.update()
        pygame.display.flip()
        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()


asyncio.run(main())
