from abc import ABC, ABCMeta
from enum import Enum
from random import randint

from pygame import Surface, SurfaceType

from assets.sounds import bg_music, tap_sound, correct_guess_sound, wrong_guess_sound, sinister_laugh_sound
from components.background_image import BackgroundImage
from components.button import Button
from components.computer_hand import ComputerHand
from components.text import Text
from scenes.jump_scare_scene import JumpScareScene
from scenes.scene_base import SceneBase
from assets.images import background_image, rock_button_image, paper_button_image, scissors_button_image, \
    hand_paper_image, hand_scissors_image, hand_rock_image
import scenes.scenes_manager as sm


class GameSelect(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class GameScene(SceneBase):
    def __init__(self, screen: Surface | SurfaceType):
        super().__init__(screen)
        self.score = 0
        self.button_clicked_count = 0

        background = BackgroundImage(screen, background_image)
        self.components.append(background)

        button_size = 100
        buttons_x_position = 150
        buttons_y_position = 470

        rock_button = Button(screen, rock_button_image, buttons_x_position, buttons_y_position, button_size,
                             button_size)
        rock_button.on_click = lambda: self.click_button(GameSelect.Rock)
        self.components.append(rock_button)
        paper_button = Button(screen, paper_button_image, buttons_x_position + button_size, buttons_y_position,
                              button_size, button_size)
        paper_button.on_click = lambda: self.click_button(GameSelect.Paper)
        self.components.append(paper_button)
        scissors = Button(screen, scissors_button_image, buttons_x_position + button_size * 2, buttons_y_position,
                          button_size, button_size)
        scissors.on_click = lambda: self.click_button(GameSelect.Scissors)
        self.components.append(scissors)

        self.hand_rock = ComputerHand(screen, hand_rock_image, 200, -500, 240, 500)
        self.components.append(self.hand_rock)
        self.hand_paper = ComputerHand(screen, hand_paper_image, 200, -500, 240, 500)
        self.components.append(self.hand_paper)
        self.hand_scissors = ComputerHand(screen, hand_scissors_image, 200, -500, 240, 500)
        self.components.append(self.hand_scissors)

        bg_music.play(-1)

        self.score_text = Text(screen, "", 10, 10, (255, 255, 255), 48)
        self.components.append(self.score_text)

    def click_button(self, user_select: GameSelect):
        self.change_button_click_count()
        tap_sound.play()

        computer_select = GameSelect(randint(1, 3))

        self.move_computer_hand(computer_select)
        self.who_win(user_select, computer_select)

        self.score_text.text = f"Score: {self.score}"

    def move_computer_hand(self, computer_select: GameSelect):
        if computer_select == GameSelect.Rock:
            self.hand_rock.move()
        elif computer_select == GameSelect.Paper:
            self.hand_paper.move()
        elif computer_select == GameSelect.Scissors:
            self.hand_scissors.move()

    def who_win(self, user_select: GameSelect, computer_select: GameSelect):
        if user_select == GameSelect.Rock and computer_select == GameSelect.Rock:
            correct_guess_sound.play()
        elif user_select == GameSelect.Rock and computer_select == GameSelect.Paper:
            wrong_guess_sound.play()
            self.score -= 1
        elif user_select == GameSelect.Rock and computer_select == GameSelect.Scissors:
            correct_guess_sound.play()
            self.score += 1
        elif user_select == GameSelect.Paper and computer_select == GameSelect.Rock:
            correct_guess_sound.play()
            self.score += 1
        elif user_select == GameSelect.Paper and computer_select == GameSelect.Paper:
            correct_guess_sound.play()
        elif user_select == GameSelect.Paper and computer_select == GameSelect.Scissors:
            wrong_guess_sound.play()
            self.score -= 1
        elif user_select == GameSelect.Scissors and computer_select == GameSelect.Rock:
            wrong_guess_sound.play()
            self.score -= 1
        elif user_select == GameSelect.Scissors and computer_select == GameSelect.Paper:
            correct_guess_sound.play()
            self.score += 1
        elif user_select == GameSelect.Scissors and computer_select == GameSelect.Scissors:
            correct_guess_sound.play()

    def change_button_click_count(self):
        self.button_clicked_count += 1

        if self.button_clicked_count == 20:
            sinister_laugh_sound.play()

        if self.button_clicked_count == 40:
            sm.scene = JumpScareScene(sm.screen)
