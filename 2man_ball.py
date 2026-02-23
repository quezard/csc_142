import pygame
import random

pygame.init()

# window stuff
w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Click Game")

clock = pygame.time.Clock()

# LOAD IMAGE AFTER set_mode
ball_image = pygame.image.load("images/ball.png").convert_alpha()

# Resize image if needed
ball_image = pygame.transform.scale(ball_image, (50, 50))


# text function
def draw_text(surface, text, x, y, color, size=24):
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, color)
    surface.blit(img, (x, y))


class Ball:
    def __init__(self):
        self.image = ball_image
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, w - self.rect.width)
        self.rect.y = random.randint(0, h - self.rect.height)

        self.dx = random.choice([-3, -2, 2, 3])
        self.dy = random.choice([-3, -2, 2, 3])

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left <= 0 or self.rect.right >= w:
            self.dx = -self.dx

        if self.rect.top <= 0 or self.rect.bottom >= h:
            self.dy = -self.dy

    def draw(self):
        screen.blit(self.image, self.rect)


balls = []
score = 0

start = pygame.time.get_ticks()
lastSeconds = 0
gameOver = False

running = True
while running:
    clock.tick(60)
    screen.fill((25, 25, 25))

    now = pygame.time.get_ticks()
    passed = now - start
    seconds = passed // 1000

    # add ball every second
    if seconds > lastSeconds:
        lastSeconds = seconds
        if not gameOver:
            balls.append(Ball())

    # stop at 15 seconds
    if seconds >= 15:
        gameOver = True
        balls = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not gameOver:
                pos = pygame.mouse.get_pos()
                for b in balls[:]:
                    if b.rect.collidepoint(pos):
                        score += 1
                        balls.remove(b)

    # move + draw balls
    if not gameOver:
        for b in balls:
            b.move()
            b.draw()

    # draw score + time
    draw_text(screen, "Score: " + str(score), 10, 10, (255,255,255), 28)
    draw_text(screen, "Time: " + str(seconds), 10, 40, (255,255,255), 28)

    if gameOver:
        draw_text(screen, "GAME OVER", w//2 - 90, h//2 - 30, (255,0,0), 50)
        draw_text(screen, "Final Score: " + str(score),
                  w//2 - 110, h//2 + 20, (255,255,255), 36)

    pygame.display.flip()

pygame.quit()