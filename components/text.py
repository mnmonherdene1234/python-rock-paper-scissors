from pygame import Surface, SurfaceType, font, Color
from pygame.event import Event

from components.component_base import ComponentBase


class Text(ComponentBase):

    def __init__(self, screen: Surface | SurfaceType, text: str, x: int, y: int,
                 color: tuple[int, int, int] = (0, 0, 0), font_size: int = 24):
        super().__init__(screen)
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font_size = font_size
        self.font = font.Font(None, font_size)

    def update(self):
        pass

    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        self.screen.blit(text_surface, (self.x, self.y))

    def event(self, event: Event):
        pass
