from pygame import mixer
from pygame.mixer import Sound

mixer.init()

bg_music = Sound("assets/sounds/bg-music.wav")
tap_sound = Sound("assets/sounds/tap.wav")
correct_guess_sound = Sound("assets/sounds/correct-guess.wav")
wrong_guess_sound = Sound("assets/sounds/wrong-guess.wav")
