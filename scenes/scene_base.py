from abc import ABC
from typing import List

from pygame import Surface, SurfaceType
from pygame.event import Event

from components.component_base import ComponentBase


class SceneBase(ABC):
    components: List[ComponentBase] = []

    def __init__(self, screen: Surface | SurfaceType):
        self.screen = screen

    def update(self):
        for component in self.components:
            component.update()

        for component in self.components:
            component.draw()

    def event(self, event: Event):
        for component in self.components:
            component.event(event)
