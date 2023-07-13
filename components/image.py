from pygame import Surface, SurfaceType
from pygame.event import Event
import pygame

from components.component_base import ComponentBase


class Image(ComponentBase):
    def __init__(self, screen: Surface | SurfaceType, image: Surface | SurfaceType, x: int, y: int, w: int, h: int):
        super().__init__(screen)
        self.image = pygame.transform.scale(image, (w, h))
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def event(self, event: Event):
        pass
