import pygame

pygame.init()


class Circle:
    def __init__(self, pos_x, radius, screen, speed=(-2, -2)):
        self.screen = screen
        self.circle_pos = list(pos_x)
        self.radius = radius
        self.speed = list(speed)

    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (int(self.circle_pos[0]), int(self.circle_pos[1])), self.radius)

    def move(self):
        width, height = pygame.display.get_surface().get_size()

        if self.circle_pos[0] + self.radius >= width or self.circle_pos[0] - self.radius <= 0:
            self.speed[0] *= -1
        if self.circle_pos[1] + self.radius >= height or self.circle_pos[1] - self.radius <= 0:
            self.speed[1] *= -1

        self.circle_pos[0] += self.speed[0]
        self.circle_pos[1] += self.speed[1]


class Engine:
    def __init__(self, screen_width, screen_height):
        self.__width = screen_width
        self.__height = screen_height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.background = (0, 0, 0)
        self.game_end = False
        self.circles = []

    def run(self):
        clock = pygame.time.Clock()
        while not self.game_end:
            dt = clock.tick(60) / 1000
            self.update(dt)
            self.draw()
            self.check_events()

    def update(self, dt):
        for circle in self.circles:
            circle.move()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_end = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                circle = Circle(event.pos, 10, self.__screen)
                self.circles.append(circle)

    def draw(self):
        self.__screen.fill(self.background)
        for circle in self.circles:
            circle.draw()
        pygame.display.flip()


def main():
    size = 800
    app = Engine(size, size)
    app.run()


if __name__ == "__main__":
    main()