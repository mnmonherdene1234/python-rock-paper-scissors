from enum import Enum
from random import randint

from pygame import Surface, SurfaceType

from components.background_image import BackgroundImage
from components.button import Button
from components.computer_hand import ComputerHand
from scenes.scene_base import SceneBase


class GameSelect(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class GameScene(SceneBase):
    def __init__(self, screen: Surface | SurfaceType):
        super().__init__(screen)
        self.is_selected = False

        background_image = BackgroundImage(screen, "images/background.png")
        self.components.append(background_image)

        button_size = 100
        buttons_x_position = 150
        buttons_y_position = 470

        rock_button = Button(screen, "images/rock-button.png", buttons_x_position, buttons_y_position, button_size,
                             button_size)
        rock_button.on_click = lambda: self.click_button(GameSelect.Rock)
        self.components.append(rock_button)
        paper_button = Button(screen, "images/paper-button.png", buttons_x_position + button_size, buttons_y_position,
                              button_size, button_size)
        paper_button.on_click = lambda: self.click_button(GameSelect.Paper)
        self.components.append(paper_button)
        scissors = Button(screen, "images/scissors-button.png", buttons_x_position + button_size * 2,
                          buttons_y_position, button_size, button_size)
        scissors.on_click = lambda: self.click_button(GameSelect.Scissors)
        self.components.append(scissors)

        self.hand_rock = ComputerHand(screen, "images/hand-rock.png", 200, -500, 240, 500)
        self.components.append(self.hand_rock)
        self.hand_paper = ComputerHand(screen, "images/hand-paper.png", 200, -500, 240, 500)
        self.components.append(self.hand_paper)
        self.hand_scissors = ComputerHand(screen, "images/hand-scissors.png", 200, -500, 240, 500)
        self.components.append(self.hand_scissors)

    def click_button(self, user_select: GameSelect):
        if not self.is_selected:
            print('User Type', user_select)
            computer_selected = GameSelect(randint(1, 3))
            print(computer_selected)

            if computer_selected == GameSelect.Rock:
                self.hand_rock.move()
            elif computer_selected == GameSelect.Paper:
                self.hand_paper.move()
            elif computer_selected == GameSelect.Scissors:
                self.hand_scissors.move()
