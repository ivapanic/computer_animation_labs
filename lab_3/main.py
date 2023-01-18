import pygame
from math import sqrt
from circle_generator import CircleGenerator

max_distance = 400
PURPLE = [191, 64, 191]


def calculate_distance(start, end):
    return sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)


def color(distance, max_distance):
    dist = int((max_distance - distance) * 255 / max_distance)
    return dist * PURPLE[0] / 255, dist * PURPLE[1] / 255, dist * PURPLE[2] / 255


def main():
    circles = CircleGenerator()

    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))

    running = True
    radius = 10
    width = 5
    while running:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                    running = False
                if event.key == pygame.K_UP:
                    radius += 1
                    width += 1
                if event.key == pygame.K_DOWN:
                    radius -= 1
                    width -= 1
                if event.key == pygame.K_LEFT:
                    PURPLE[0] -= 5 if PURPLE[0] > 10 else 0
                if event.key == pygame.K_RIGHT:
                    if PURPLE[0] < 240:
                        PURPLE[0] += 5

        screen.fill((0, 0, 0))

        for line in circles.connect_circles():
            distance = calculate_distance(line[0], line[1])

            if distance < max_distance:
                pygame.draw.line(screen, color(distance, max_distance), start_pos=line[0], end_pos=line[1], width=width)

        for circle in circles.circles:
            pygame.draw.circle(screen, PURPLE, center=circle[:2], radius=radius)

        circles.update()

        pygame.display.update()


if __name__ == "__main__":
    main()