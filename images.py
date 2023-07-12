import pygame

background_image = pygame.image.load("images/background.png")

button_size = 100
rock_button = pygame.image.load("images/rock-button.png")
rock_button = pygame.transform.scale(rock_button, (button_size, button_size))
paper_button = pygame.image.load("images/paper-button.png")
paper_button = pygame.transform.scale(paper_button, (button_size, button_size))
scissors_button = pygame.image.load("images/scissors-button.png")
scissors_button = pygame.transform.scale(scissors_button, (button_size, button_size))