from enum import Enum
import random
import pygame


class Wind(Enum):
    EAST = -2
    NONE = -1
    WEST = +2


class Snow:
    def __init__(self, snowflakes, window, Wind):
        self.snowflakes = snowflakes
        self.window = window
        self.wind = Wind.value
        self.velocity = 0.01
        self.snowflake_img = pygame.image.load("snowflake.png")

    def starting_point(self):
        return random.randint(0, 1080)

    def particles_generator(self):
        self.snowflakes.append([
            [self.starting_point(), 0],
            [random.randint(0, 10) / 10 + self.wind, 2],
            random.randint(5, 35), False])
        ground = random.randint(850, 900)
        for snowflake in self.snowflakes:
            if snowflake[0][1] <= ground:
                snowflake[0][0] += snowflake[1][0]
                snowflake[0][1] += snowflake[1][1]
                snowflake[1][1] += self.velocity
            elif snowflake[0][1] >= ground:
                snowflake[1][1] = 0
                snowflake[1][0] = 0
                snowflake[3] = True
            snowflake[2] -= 0.005
            if snowflake[2] <= 0:
                self.snowflakes.remove(snowflake)

        for snowflake in self.snowflakes:
            self.window.blit(pygame.transform.scale(self.snowflake_img, (snowflake[2], snowflake[2])),
                        (snowflake[0][0], snowflake[0][1]))

