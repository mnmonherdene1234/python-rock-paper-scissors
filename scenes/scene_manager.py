from pygame import Surface, SurfaceType
from pygame.event import Event

from scenes.scene_base import SceneBase

screen: Surface | SurfaceType
scene: SceneBase


def update():
    scene.update()


def event(game_event: Event):
    scene.event(game_event)
