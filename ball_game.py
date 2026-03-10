import pygame
import random

pygame.init()
pygame.mixer.init()

# Window setup
w = 800
h = 600
window = pygame.display.set_mode((w, h))
pygame.display.set_caption("Click the Ball Game")

clock = pygame.time.Clock()

# Load image AFTER set_mode
ball_image = pygame.image.load("images/ball.png").convert_alpha()

# Optional resize (adjust size if needed)
ball_image = pygame.transform.scale(ball_image, (60, 60))

# Load sound
success_sound = pygame.mixer.Sound("success.wav")


# Helper function
def draw_text(surface, text, x, y, color, font_size=24):
    text_font = pygame.font.SysFont(None, font_size)
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)


class Ball:
    def __init__(self):
        self.image = ball_image
        self.rect = self.image.get_rect()

        self.reset_position()

        self.dx = random.choice([-3, 3])
        self.dy = random.choice([-3, 3])

    def reset_position(self):
        self.rect.x = random.randint(0, w - self.rect.width)
        self.rect.y = random.randint(0, h - self.rect.height)

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Bounce off walls
        if self.rect.left <= 0 or self.rect.right >= w:
            self.dx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= h:
            self.dy *= -1

    def draw(self):
        window.blit(self.image, self.rect)


# Game variables
ball = Ball()
score = 0
game_over = False

# Record start time
start_time = pygame.time.get_ticks()

running = True
while running:
    clock.tick(60)
    window.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if ball.rect.collidepoint(event.pos):
                score += 1
                success_sound.play()

                # Increase speed randomly between 1 and 5
                increase_x = random.randint(1, 5)
                increase_y = random.randint(1, 5)

                ball.dx = (abs(ball.dx) + increase_x) * (1 if ball.dx > 0 else -1)
                ball.dy = (abs(ball.dy) + increase_y) * (1 if ball.dy > 0 else -1)

                ball.reset_position()

                if score == 5:
                    game_over = True
                    end_time = pygame.time.get_ticks()

    if not game_over:
        ball.move()
        ball.draw()

    # Draw score top-left
    draw_text(window, f"Score: {score}", 10, 10, (255, 255, 255), 28)

    if game_over:
        total_time = (end_time - start_time) / 1000
        draw_text(window, "GAME OVER!", w//2 - 130, h//2 - 40, (255, 0, 0), 48)
        draw_text(window, f"Time: {total_time:.2f} seconds",
                  w//2 - 150, h//2 + 10, (255, 255, 255), 36)

    pygame.display.flip()

pygame.quit()