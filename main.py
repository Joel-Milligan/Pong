import pygame
import colours
import paddle
import ball

# Variables
running = True
game_state = "playing"
winning_player = None
screen_size = (800, 600)
screen_title = "Pong"
indent = 50

# Initialisation
pygame.init()
main_display = pygame.display.set_mode(screen_size)
pygame.display.set_caption(screen_title)
clock = pygame.time.Clock()
game_ball = ball.Ball(main_display, screen_size[0] / 2, screen_size[1] / 2)
player_right = paddle.Paddle(main_display, \
                        screen_size[0] - (indent + paddle.Paddle.width), \
                        (screen_size[1] / 2) - (paddle.Paddle.height - 2))
player_left = paddle.Paddle(main_display, \
                        (indent + paddle.Paddle.width), \
                        (screen_size[1] / 2) - (paddle.Paddle.height - 2))

# Functions
def held_keys(keys):
    if keys[pygame.K_w]:
        player_right.move_up()

    if keys[pygame.K_s]:
        player_right.move_down()

    if keys[pygame.K_UP]:
        player_left.move_up()

    if keys[pygame.K_DOWN]:
        player_left.move_down()

def game_win(winner):
    pygame.time.delay(1000)
    pygame.quit()
    quit()

def check_ball_collision():
    # Check if hit a paddle
    # TODO Deal with when the ball hits top/bottom of paddle
    if(game_ball.rect.colliderect(player_right.rect) or game_ball.rect.colliderect(player_left.rect)):
        game_ball.reflect_x()

    # Bounce if hit top/bottom
    if not((game_ball.rect.top) > 0 and (game_ball.rect.bottom) < screen_size[1]):
        game_ball.reflect_y()

    # Check if ball went out of screen
    if(game_ball.rect.left >= screen_size[0]):
        game_win(player_left)
    
    if(game_ball.rect.right <= 0):
        game_win(player_right)

def update_screen():
    if(game_state == "playing"):
    main_display.fill(colours.black)
    player_right.draw()
    player_left.draw()
    check_ball_collision()
    game_ball.update_position()
    game_ball.draw()
    pygame.display.flip()

    if(game_state == "win"):
        game_win(winning_player)

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
