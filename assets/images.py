import sys
from pygame import image

if getattr(sys, 'frozen', False):
    # Running as a bundled executable
    base_path = f'{sys._MEIPASS}/'
else:
    # Running in a development environment
    base_path = ''

game_icon = image.load(f"{base_path}assets/images/icon.png")
background_image = image.load(f"{base_path}assets/images/background.png")
hand_paper_image = image.load(f"{base_path}assets/images/hand-paper.png")
hand_rock_image = image.load(f"{base_path}assets/images/hand-rock.png")
hand_scissors_image = image.load(f"{base_path}assets/images/hand-scissors.png")
paper_button_image = image.load(f"{base_path}assets/images/paper-button.png")
rock_button_image = image.load(f"{base_path}assets/images/rock-button.png")
scissors_button_image = image.load(f"{base_path}assets/images/scissors-button.png")
scary_background_image = image.load(f"{base_path}assets/images/scary-background.png")
cat_image = image.load(f"{base_path}assets/images/cat.png")
exit_button_image = image.load(f"{base_path}assets/images/exit-button.png")
