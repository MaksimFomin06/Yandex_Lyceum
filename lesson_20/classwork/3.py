import pygame


class Haul:
    def __init__(self, screen_width: int = 300, screen_height: int = 300):
        pygame.init()
        self.width = screen_width
        self.height = screen_height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = (0, 0, 0)
        self.game_end = False

        self.green = (0, 255, 0)
        self.size = (100, 100)
        self.pos = (0, 0)
        self.haul = False
        self.offset = (0, 0)

    def run(self):
        while not self.game_end:
            self.check_events()
            self.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_end = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.check_pos(mouse_pos):
                        self.haul = True
                        self.offset = (mouse_pos[0] - self.pos[0],
                                       mouse_pos[1] - self.pos[1])
            elif event.type == pygame.MOUSEMOTION:
                if self.haul:
                    mouse_pos = pygame.mouse.get_pos()
                    self.pos = (mouse_pos[0] - self.offset[0],
                                mouse_pos[1] - self.offset[1])
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.haul = False

    def check_pos(self, mouse_pos):
        x, y = self.pos
        w, h = self.size
        return (x <= mouse_pos[0] <= x + w) and (y <= mouse_pos[1] <= y + h)

    def draw(self):
        self.screen.fill(self.background)
        pygame.draw.rect(self.screen, self.green, (self.pos, self.size))
        pygame.display.flip()


def main():
    app = Haul()
    app.run()


if __name__ == "__main__":
    main()