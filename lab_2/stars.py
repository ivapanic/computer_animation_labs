from enum import Enum
import random
import pygame

class Star:
    def __init__(self, stars, window):
        self.stars = stars
        self.window = window
        self.star_img = pygame.image.load("star.png")
        self.ratio = 0.2

    def starting_point(self):
        return [random.randint(0, 1080), random.randint(0, 500)]

    def particles_generator(self):
        smaller = False
        if len(self.stars) < 100:
            self.stars.append([
                self.starting_point(), random.randint(5, 25)])
        for star in self.stars:
            if not smaller:
                star[1] += self.ratio
                if star[1] >= 25:
                    smaller = True
            if smaller:
                if star[1] >= 5:
                    star[1] -= self.ratio
                else:
                    smaller = False
        for star in self.stars:
            self.window.blit(pygame.transform.scale(self.star_img, (star[1], star[1])),
                        (star[0][0], star[0][1]))

