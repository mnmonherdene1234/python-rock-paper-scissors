import sys
from pygame import mixer
from pygame.mixer import Sound

if getattr(sys, 'frozen', False):
    # Running as a bundled executable
    base_path = f'{sys._MEIPASS}/'
else:
    # Running in a development environment
    base_path = ''

mixer.init()

bg_music = Sound(f"{base_path}assets/sounds/bg-music.wav")
tap_sound = Sound(f"{base_path}assets/sounds/tap.wav")
correct_guess_sound = Sound(f"{base_path}assets/sounds/correct-guess.wav")
wrong_guess_sound = Sound(f"{base_path}assets/sounds/wrong-guess.wav")
scary_sound_effect = Sound(f"{base_path}assets/sounds/scary-effect.ogg")
sinister_laugh_sound = Sound(f"{base_path}assets/sounds/sinister-laugh.ogg")
scary_background_sound = Sound(f"{base_path}assets/sounds/scary-background-sound.ogg")
knocking_sound_effect = Sound(f"{base_path}assets/sounds/knocking-sound-effect.ogg")
meow_meow_nigga_sound = Sound(f"{base_path}assets/sounds/meow-meow-nigga.ogg")
