import pygame
import random

# --- Constants ---
WIDTH = 800
HEIGHT = 600
FPS = 60

# --- Base Class ---
class Animal:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.x += random.randint(-1, 1) * self.speed
        self.y += random.randint(-1, 1) * self.speed

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 5)

# --- Prey Class ---
class Prey(Animal):
    def update(self):
        self.move()

# --- Predator Class ---
class Predator(Animal):
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed)
        self.energy = 100

    def update(self):
        self.move()
        self.energy -= 0.1

# --- Simulation Manager ---
class Simulation:
    def __init__(self):
        self.prey_list = [Prey(random.randint(0, WIDTH), random.randint(0, HEIGHT), 2) for _ in range(20)]
        self.predators = [Predator(random.randint(0, WIDTH), random.randint(0, HEIGHT), 3) for _ in range(5)]

    def update(self):
        for prey in self.prey_list:
            prey.update()

        for predator in self.predators:
            predator.update()

    def draw(self, screen):
        for prey in self.prey_list:
            prey.draw(screen, (0, 255, 0))  # green

        for predator in self.predators:
            predator.draw(screen, (255, 0, 0))  # red

# --- Main Game ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    sim = Simulation()

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        sim.update()
        sim.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()