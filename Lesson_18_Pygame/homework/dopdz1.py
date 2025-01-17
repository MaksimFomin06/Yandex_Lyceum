import pygame


class Cube:
    def __init__(self, cube_sides, hue):
        self.__width = 300
        self.__height = 300
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.game_end = False

        self.cube_sides = cube_sides
        self.hue = hue
        self.center = (self.__width // 2 - self.cube_sides // 2, self.__height // 2, self.cube_sides, self.cube_sides)

    def run(self):
        while not self.game_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_end = True
            self.draw()

    def draw(self):
        pygame.draw.rect(self.__screen, (255, 0, 0), self.center)
        pygame.display.flip()


def main():
    try:
        cube_sides, hue = map(int, input().split())
        app = Cube(cube_sides, hue)
        app.run()
    except ValueError:
        print("Неверный формат данных.")


if __name__ == "__main__":
    main()