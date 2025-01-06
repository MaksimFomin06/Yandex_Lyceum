import pygame


class Tail:
    def __init__(self, screen_width=501, screen_height=501):
        self.width = screen_width
        self.height = screen_height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.game_end = False
        self.fps = 60
        self.clock = pygame.time.Clock()

        self.color = (255, 0, 0)
        self.pos = (self.width // 2, self.height // 2)
        self.radius = 20
        self.speed = 2

        self.target_pos = self.pos
        self.moving = False

    def run(self):
        while not self.game_end:
            self.draw()
            self.check_events()
            if self.moving:
                self.move()
            self.clock.tick(self.fps)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_end = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.target_pos = event.pos
                self.moving = True

    def move(self):
        dx = self.target_pos[0] - self.pos[0]
        dy = self.target_pos[1] - self.pos[1]
        distance = max(abs(dx), abs(dy))

        if distance > 0:
            step_x = self.speed * dx / distance
            step_y = self.speed * dy / distance
            self.pos = (self.pos[0] + step_x, self.pos[1] + step_y)

            if abs(dx) <= 1 and abs(dy) <= 1:
                self.pos = self.target_pos
                self.moving = False

    def draw(self):
        self.screen.fill((0 ,0, 0))
        pygame.draw.circle(self.screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)
        pygame.display.flip()


def main():
    pygame.init()
    app = Tail()
    app.run()
    pygame.quit()


if __name__ == "__main__":
    main()