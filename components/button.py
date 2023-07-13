import pygame
from pygame import Surface, SurfaceType
from pygame.event import Event

from components.component_base import ComponentBase


class Button(ComponentBase):
    def __init__(self, screen: Surface | SurfaceType, image: Surface | SurfaceType, x: int, y: int, w: int, h: int):
        super().__init__(screen)
        self.image = pygame.transform.scale(image, (w, h))
        self.rect = pygame.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.w = self.w
        self.rect.h = self.h

    def event(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and event.button == 1:
                self.on_click()

    def on_click(self):
        pass
