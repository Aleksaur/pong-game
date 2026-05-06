import pygame
import sys

# --- SETUP ---
pygame.init()

WIDTH, HEIGHT = 1000, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

TEXT_COLOR = (225, 255, 225)
BG_COLOR = (30, 30, 30)

text_font = pygame.font.SysFont(None, 75)
score_font = pygame.font.SysFont(None, 150)

game_over_text = text_font.render("Game Over", True, TEXT_COLOR)

# --- GAME STATE ---
score = 0

player1 = pygame.Rect(WIDTH - 15, 350, 7, 75)
player2 = pygame.Rect(10, 350, 7, 75)
paddle_speed = 6

ball = pygame.Rect(WIDTH // 2 - 6, HEIGHT // 2 - 6, 12, 12)
ball_speed_x = 4
ball_speed_y = 4


# --- FUNCTIONS ---
def draw(score_surface):
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, TEXT_COLOR, player1)
    pygame.draw.rect(screen, TEXT_COLOR, player2)
    pygame.draw.ellipse(screen, TEXT_COLOR, ball)
    screen.blit(score_surface, (WIDTH // 2 - 25, HEIGHT // 2 - 75))
    pygame.display.flip()


def move_paddles():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player1.y -= paddle_speed
    if keys[pygame.K_DOWN]:
        player1.y += paddle_speed
    if keys[pygame.K_w]:
        player2.y -= paddle_speed
    if keys[pygame.K_s]:
        player2.y += paddle_speed

    # clamp to screen
    player1.clamp_ip(screen.get_rect())
    player2.clamp_ip(screen.get_rect())


def move_ball():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1


def reset_round():
    global ball_speed_x, ball_speed_y, score

    pygame.time.wait(500)
    screen.fill(BG_COLOR)
    screen.blit(game_over_text, (350, 350))
    pygame.display.flip()

    pygame.time.wait(3000)

    score = 0
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x *= -1


# --- MAIN LOOP ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    move_paddles()
    move_ball()

    # score surface updated once per frame
    score_surface = score_font.render(str(score), True, (130, 150, 130))

    # wall (left/right) = lose
    if ball.left <= 0 or ball.right >= WIDTH:
        reset_round()

    # paddle collision
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
        score += 1

    draw(score_surface)
    clock.tick(60)

pygame.quit()
sys.exit()
