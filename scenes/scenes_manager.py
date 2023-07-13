import pygame
from pygame import Surface, SurfaceType

from scenes.game_scene import GameScene
from scenes.jump_scare_scene import JumpScareScene
from scenes.scene_base import SceneBase

running = True
screen: Surface | SurfaceType
scene: SceneBase

game_scene: GameScene
jump_scare_scene: JumpScareScene


def init(game_screen: Surface | SurfaceType):
    global game_scene, jump_scare_scene, screen, scene
    screen = game_screen
    game_scene = GameScene(game_screen)
    scene = game_scene


def update():
    global scene
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global running
            running = False

        scene.components_event(event)
        scene.event(event)

    scene.components_update()
    scene.update()
