import pygame, sys, time

pygame.init()
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
text_font = pygame.font.SysFont(None, 75)
score_font = pygame.font.SysFont(None, 150)
text = text_font.render("Game Over", True, (225, 255, 225))
score = 0
show_score = score_font.render(str(score), True, (130, 150, 130))

player1 = pygame.Rect(985, 350, 7, 75)
player2 = pygame.Rect(10,  350, 7, 75)
paddle_speed = 6

ball = pygame.Rect(495, 370, 12, 12)
ball_speed_x = 4
ball_speed_y = 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player1.y -= paddle_speed
    if keys[pygame.K_DOWN]:
        player1.y += paddle_speed
    if keys[pygame.K_w]:
        player2.y -= paddle_speed
    if keys[pygame.K_s]:
        player2.y += paddle_speed


    if player1.top < 0: player1.top = 0
    if player1.bottom > 750: player1.bottom = 750
    if player2.top < 0: player2.top = 0
    if player2.bottom > 750: player2.bottom = 750

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= 750:
        ball_speed_y *= -1

    if ball.left <= 0 or ball.right >= 1000:
        pygame.time.wait(500)
        screen.fill((30, 30, 30))
        screen.blit(text, (350, 350))
        score = 0
        show_score = score_font.render(str(score), True, (130, 150, 130))
        pygame.display.flip()
        pygame.time.wait(3000)
        ball.x = 495
        ball.y = 370
        ball_speed_x *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        score += 1
        show_score = score_font.render(str(score), True, (130, 150, 130))
        ball_speed_x *= -1

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (225, 255, 225), player1)
    pygame.draw.rect(screen, (225, 255, 225), player2)
    pygame.draw.ellipse(screen, (225, 255, 225), ball)
    screen.blit(show_score, (475, 300))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
