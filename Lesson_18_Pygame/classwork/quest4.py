import pygame

class Target:
    def __init__(self, circle_weight, num_of_rings):
        pygame.init()
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.game_end = False

        self.circle_weight = circle_weight
        self.num_of_rings = num_of_rings
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    def run(self):
        while not self.game_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_end = True
            self.draw()
    
    def draw(self):
        x_center = self.circle_weight // 2
        y_center = self.circle_weight // 2
        
        current_color_index = 0
        for ring in range(self.num_of_rings):
            pygame.draw.circle(
                self.screen,
                self.colors[current_color_index],
                (x_center, y_center),
                (ring + 1) * self.circle_weight,
                self.circle_weight
            )
            
            current_color_index = (current_color_index + 1) % len(self.colors)
        
        pygame.display.flip()


def main():
    circle_weight, num_of_rings = map(int, input().split())
    if circle_weight <= 0 or num_of_rings <= 0:
        print("Неправильный формат ввода")
    else:
        app = Target(circle_weight, num_of_rings)
        app.run()
        
        
if __name__ == "__main__":
    main()