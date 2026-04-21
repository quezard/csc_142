import pygame
import random
import math

# --- Constants ---
WIDTH = 800
HEIGHT = 600
FPS = 60

# --- Button Class ---
class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, screen, font):
        pygame.draw.rect(screen, (50, 50, 50), self.rect)
        pygame.draw.rect(screen, (200, 200, 200), self.rect, 2)

        label = font.render(self.text, True, (255, 255, 255))
        screen.blit(label, (self.rect.x + 10, self.rect.y + 5))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# --- Base Class ---
class Animal:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move_random(self):
        self.x += random.randint(-1, 1) * self.speed
        self.y += random.randint(-1, 1) * self.speed
        self.stay_in_bounds()

    def stay_in_bounds(self):
        self.x = max(0, min(WIDTH, self.x))
        self.y = max(0, min(HEIGHT, self.y))

    def draw(self, screen, color, size=5):
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), size)


# --- Prey ---
class Prey(Animal):
    def update(self, predators):
        if predators:
            self.flee(predators)
        else:
            self.move_random()

    def flee(self, predators):
        closest = min(predators, key=lambda p: (p.x - self.x)**2 + (p.y - self.y)**2)

        dx = self.x - closest.x
        dy = self.y - closest.y
        dist = max(1, math.hypot(dx, dy))

        self.x += self.speed * dx / dist
        self.y += self.speed * dy / dist
        self.stay_in_bounds()


# --- Predator ---
class Predator(Animal):
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed)
        self.energy = 100

    def update(self, prey_list):
        if prey_list:
            self.chase(prey_list)
        else:
            self.move_random()

        self.energy -= 0.2
        self.stay_in_bounds()

    def chase(self, prey_list):
        closest = min(prey_list, key=lambda p: (p.x - self.x)**2 + (p.y - self.y)**2)

        dx = closest.x - self.x
        dy = closest.y - self.y
        dist = max(1, math.hypot(dx, dy))

        self.x += self.speed * dx / dist
        self.y += self.speed * dy / dist


# --- Simulation ---
class Simulation:
    def __init__(self):
        self.reset()

    def reset(self):
        self.prey_list = [Prey(random.randint(0, WIDTH), random.randint(0, HEIGHT), 2) for _ in range(20)]
        self.predators = [Predator(random.randint(0, WIDTH), random.randint(0, HEIGHT), 3) for _ in range(5)]
        self.score = 0

    def update(self):
        for prey in self.prey_list:
            prey.update(self.predators)

        for predator in self.predators:
            predator.update(self.prey_list)

        # Eating
        for predator in self.predators:
            for prey in self.prey_list[:]:
                if math.hypot(predator.x - prey.x, predator.y - prey.y) < 10:
                    self.prey_list.remove(prey)
                    predator.energy += 25
                    self.score += 1

        # Remove dead predators
        self.predators = [p for p in self.predators if p.energy > 0]

        # Spawn prey
        if random.random() < 0.02:
            self.prey_list.append(Prey(random.randint(0, WIDTH), random.randint(0, HEIGHT), 2))

    def draw(self, screen, font):
        for prey in self.prey_list:
            prey.draw(screen, (0, 255, 0), 4)

        for predator in self.predators:
            size = max(4, int(predator.energy / 20))
            predator.draw(screen, (255, 0, 0), size)

        # UI Text
        screen.blit(font.render(f"Prey: {len(self.prey_list)}", True, (255,255,255)), (10,10))
        screen.blit(font.render(f"Predators: {len(self.predators)}", True, (255,255,255)), (10,40))
        screen.blit(font.render(f"Score: {self.score}", True, (255,255,0)), (10,70))


# --- Main ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Predator-Prey Simulation")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)

    sim = Simulation()

    # Buttons
    start_btn = Button(600, 10, 80, 30, "Start")
    pause_btn = Button(600, 50, 80, 30, "Pause")
    reset_btn = Button(600, 90, 80, 30, "Reset")

    running = True
    sim_running = False

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # Button clicks
                if start_btn.is_clicked(pos):
                    sim_running = True
                elif pause_btn.is_clicked(pos):
                    sim_running = False
                elif reset_btn.is_clicked(pos):
                    sim.reset()
                    sim_running = False

                else:
                    # User controls
                    if event.button == 1:  # Left click = add prey
                        sim.prey_list.append(Prey(pos[0], pos[1], 2))
                    elif event.button == 3:  # Right click = add predator
                        sim.predators.append(Predator(pos[0], pos[1], 3))

        if sim_running:
            sim.update()

        sim.draw(screen, font)

        # Draw buttons
        start_btn.draw(screen, font)
        pause_btn.draw(screen, font)
        reset_btn.draw(screen, font)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()