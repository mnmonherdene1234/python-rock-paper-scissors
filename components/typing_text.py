from pygame import Surface, SurfaceType

from components.text import Text


class TypingText(Text):
    def __init__(self, screen: Surface | SurfaceType, text: str, x: int, y: int,
                 color: tuple[int, int, int] = (0, 0, 0), font_size: int = 24):
        super().__init__(screen, text, x, y, color, font_size)
        self.current_text = ""
        self.time = 0
        self.index = 0

    def update(self):
        if len(self.text) > self.index:
            self.time += 1

            if self.time % 30 == 0:
                self.current_text += self.text[self.index]
                self.index += 1

    def draw(self):
        text_surface = self.font.render(self.current_text, True, self.color)
        self.screen.blit(text_surface, (self.x, self.y))
