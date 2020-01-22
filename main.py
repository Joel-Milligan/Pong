import pygame
import colours
import paddle
import ball

# Variables
running = True
screen_size = (800, 600)
indent = 50

# Initialisation
pygame.init()
main_display = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
game_ball = ball.Ball(main_display, screen_size[0] / 2, screen_size[1] / 2)
player1 = paddle.Paddle(main_display, \
                        screen_size[0] - (indent + paddle.Paddle.width), \
                        (screen_size[1] / 2) - (paddle.Paddle.height - 2))
player2 = paddle.Paddle(main_display, \
                        (indent + paddle.Paddle.width), \
                        (screen_size[1] / 2) - (paddle.Paddle.height - 2))

# Functions
def held_keys(keys):
    if keys[pygame.K_w]:
        player1.move_up()

    if keys[pygame.K_s]:
        player1.move_down()

    if keys[pygame.K_UP]:
        player2.move_up()

    if keys[pygame.K_DOWN]:
        player2.move_down()

def check_ball_collision():
    # Check if hit a paddle
    if(game_ball.rect.colliderect(player1.rect) or game_ball.rect.colliderect(player2.rect)):
        game_ball.reflect_x()

    # Bounce if hit top/bottom
    if not((game_ball.rect.top) > 0 and (game_ball.rect.bottom) < screen_size[1]):
        game_ball.reflect_y()

def update_screen():
    main_display.fill(colours.black)
    player1.draw()
    player2.draw()
    check_ball_collision()
    game_ball.update_position()
    game_ball.draw()
    pygame.display.flip()

# Main Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    held_keys(pygame.key.get_pressed())

    update_screen()
    clock.tick(60)

pygame.quit()
quit()
