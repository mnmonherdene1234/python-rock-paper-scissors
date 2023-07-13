import pygame
from pygame import Surface, SurfaceType

from scenes.scene_base import SceneBase

running = True
screen: Surface | SurfaceType
scene: SceneBase


def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global running
            running = False

        scene.event(event)

    scene.update()
