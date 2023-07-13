from pygame import Surface, SurfaceType

from assets.images import scary_background_image, cat_image, exit_button_image
from assets.sounds import bg_music, scary_background_sound, knocking_sound_effect, meow_meow_nigga_sound, tap_sound
from components.background_image import BackgroundImage
from components.button import Button
from components.image import Image
from components.typing_text import TypingText
from scenes.scene_base import SceneBase
import scenes.scenes_manager as sm


class JumpScareScene(SceneBase):
    def __init__(self, screen: Surface | SurfaceType):
        super().__init__(screen)
        self.time = 0
        self.background = BackgroundImage(screen, scary_background_image)
        self.components.append(self.background)
        self.start()

    def start(self):
        bg_music.stop()
        scary_background_sound.play(-1)

    def update(self):
        self.time += 1

        if self.time == 1000:
            knocking_sound_effect.play()

        if self.time == 2000:
            cat = Image(self.screen, cat_image, 270, 300, 100, 100)
            self.components.append(cat)
            tap_sound.play()

        if self.time == 2500:
            meow_meow_nigga_sound.play()

        if self.time == 3000:
            thank_you_for_playing = TypingText(self.screen, "Thank you for playing", 120, 100, (255, 255, 255), 48)
            self.components.append(thank_you_for_playing)

        if self.time == 3500:
            exit_button = Button(self.screen, exit_button_image, 200, 450, 190, 70)

            def exit_button_click():
                tap_sound.play()
                sm.running = False

            exit_button.on_click = exit_button_click
            self.components.append(exit_button)
