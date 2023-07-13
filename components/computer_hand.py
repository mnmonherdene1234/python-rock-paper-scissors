from pygame import Surface, SurfaceType

from components.image import Image


class ComputerHand(Image):

    def __init__(self, screen: Surface | SurfaceType, image_path: str, x: int, y: int, w: int, h: int):
        super().__init__(screen, image_path, x, y, w, h)
        self.__is_moving = False
        self.__is_moving_back = False
        self.__initial_y = y
        self.__speed = 3

    def move(self):
        if not self.__is_moving:
            self.__is_moving = True

    def update(self):
        if self.__is_moving:
            if self.y > 0:
                self.__is_moving_back = True

            if self.y < self.__initial_y:
                self.__is_moving = False
                self.y = self.__initial_y

            if self.__is_moving_back:
                self.y -= self.__speed
            else:
                self.y += self.__speed
