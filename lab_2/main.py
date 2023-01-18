import pygame
from snow import Snow, Wind
from stars import Star

pygame.init()
trees = pygame.image.load("trees.png")

window = pygame.display.set_mode((1080, 900))
clock = pygame.time.Clock()
snowflakes = []
stars = []


def main():
    snow = Snow(snowflakes, window, Wind.NONE)
    star = Star(stars, window)

    while True:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                    snow.wind = Wind.EAST.value if e.key == pygame.K_LEFT else Wind.WEST.value
                elif e.key == pygame.K_SPACE:
                    snow.wind = Wind.NONE.value
                elif e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                    for flake in snowflakes:
                        if not flake[3]:
                            flake[2] += 1 if e.key == pygame.K_UP else -1


        window.fill((0, 0, 0))
        window.blit(trees, (0, 0))
        snow.particles_generator()
        star.particles_generator()
        pygame.display.update()

if __name__ == '__main__':
    main()
