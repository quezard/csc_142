import pygame
import random

# -----------------------------
# Raindrop Class (Part 2)
# -----------------------------
class Raindrop:
    __slots__ = ['x', 'y', 'radius']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1

    def update(self):
        self.radius += 1

    def draw(self, window):
        pygame.draw.circle(window, (0, 0, 255), (self.x, self.y), self.radius)


# -----------------------------
# Raindrops Manager (Part 1, 3, 4)
# -----------------------------
class RaindropsManager:
    RAIN_RATE = 300        # milliseconds between drops
    MAX_RADIUS = 50        # max size before removal

    def __init__(self):
        pygame.init()
        self.width = 600
        self.height = 400
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Raindrops on Glass")

        self.clock = pygame.time.Clock()
        self.raindrops = []

        self.last_drop_time = pygame.time.get_ticks()

    def run(self):
        running = True

        while running:
            current_time = pygame.time.get_ticks()

            # --- Events ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # --- Add Raindrops (Part 3) ---
            if current_time - self.last_drop_time > RaindropsManager.RAIN_RATE:
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
                self.raindrops.append(Raindrop(x, y))
                self.last_drop_time = current_time

            # --- Update Raindrops ---
            for drop in self.raindrops:
                drop.update()

            # --- Remove Large Raindrops (Part 4) ---
            self.raindrops = [
                drop for drop in self.raindrops
                if drop.radius <= RaindropsManager.MAX_RADIUS
            ]

            # --- Draw ---
            self.window.fill((230, 230, 230))  # light gray background

            for drop in self.raindrops:
                drop.draw(self.window)

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()


# -----------------------------
# Driver Code
# -----------------------------
def main():
    manager = RaindropsManager()
    manager.run()


if __name__ == "__main__":
    main()