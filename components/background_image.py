from pygame import Surface, SurfaceType
from pygame.event import Event

from components.component_base import ComponentBase


class BackgroundImage(ComponentBase):
    def __init__(self, screen: Surface | SurfaceType, image: Surface | SurfaceType):
        super().__init__(screen)
        self.image = image

    def draw(self):
        self.screen.blit(self.image, (0, 0))

    def event(self, event: Event):
        pass

    def update(self):
        pass
