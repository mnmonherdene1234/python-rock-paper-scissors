from pygame import Surface, SurfaceType
from pygame.event import Event
import abc


class ComponentBase(abc.ABC):
    def __init__(self, screen: Surface | SurfaceType):
        self.screen = screen

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def event(self, event: Event):
        pass
