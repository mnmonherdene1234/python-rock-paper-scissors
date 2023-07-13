from pygame import Surface, SurfaceType
import pygame
from pygame.event import Event

from components.component_base import ComponentBase


class BackgroundImage(ComponentBase):
    def __init__(self, screen: Surface | SurfaceType, image_path: str):
        super().__init__(screen)
        self.image = pygame.image.load(image_path)

    def draw(self):
        self.screen.blit(self.image, (0, 0))

    def event(self, event: Event):
        pass

    def update(self):
        pass
