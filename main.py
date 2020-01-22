import pygame
import colours
import paddle
import ball

# Variables
running = True
game_state = "menu"
winning_player = None
left_score = 0
right_score = 0

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

# Text
font = pygame.font.SysFont(None, 72)

start_game_text = font.render("Start Game", True, colours.white, colours.black)
start_text_x = (screen_size[0] / 2) - (start_game_text.get_width() / 2)
start_text_y = (screen_size[1] / 3) - (start_game_text.get_height() / 2)
start_button = pygame.Rect(start_text_x, start_text_y, start_game_text.get_width(), start_game_text.get_height())

quit_text = font.render("Quit", True, colours.white, colours.black)
quit_text_x = (screen_size[0] / 2) - (quit_text.get_width() / 2)
quit_text_y = (2 * screen_size[1] / 3) - (quit_text.get_height() / 2)
quit_button = pygame.Rect(quit_text_x, quit_text_y, quit_text.get_width(), quit_text.get_height())

score_indent = 75

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

def mouse_clicked(position):
    global game_state

    if(game_state == "menu"):
        if(start_button.collidepoint(position)):
            game_state = "playing"
        elif(quit_button.collidepoint(position)):
            pygame.quit()
            quit()

def reset_ball():
    global game_ball
    game_ball = ball.Ball(main_display, screen_size[0] / 2, screen_size[1] / 2)

def score(player):
    global left_score
    global right_score
    global game_ball

    if player == player_left:
        left_score += 1
        reset_ball()
    if player == player_right:
        right_score += 1
        reset_ball()

def check_ball_collision():
    global game_state
    global winning_player

    # Check if hit a paddle
    # TODO Deal with when the ball hits top/bottom of paddle
    if(game_ball.rect.colliderect(player_right.rect) or game_ball.rect.colliderect(player_left.rect)):
        game_ball.reflect_x()

    # Bounce if hit top/bottom
    if not((game_ball.rect.top) > 0 and (game_ball.rect.bottom) < screen_size[1]):
        game_ball.reflect_y()

    # Check if ball went out of screen
    if(game_ball.rect.left >= screen_size[0]):
        score(player_left)
    
    if(game_ball.rect.right <= 0):
        score(player_right)

def update_screen():
    if(game_state == "menu"):
        main_display.fill(colours.black)
        main_display.blit(start_game_text, start_button)
        main_display.blit(quit_text, quit_button)

        pygame.display.flip()
    
    if(game_state == "playing"):
        global right_score
        global left_score
        
        main_display.fill(colours.black)
        player_right.draw()
        player_left.draw()
        check_ball_collision()
        
        left_score_text = font.render(str(left_score), True, colours.white, colours.black)
        left_score_x = (screen_size[0] / 3) - (left_score_text.get_width() / 2)
        left_score_y = score_indent
        left_score_rect = pygame.Rect(left_score_x, left_score_y, left_score_text.get_width(), left_score_text.get_height())
        main_display.blit(left_score_text, left_score_rect)

        right_score_text = font.render(str(right_score), True, colours.white, colours.black)
        right_score_x = (2 * screen_size[0] / 3) - (right_score_text.get_width() / 2)
        right_score_y = score_indent
        right_score_rect = pygame.Rect(right_score_x, right_score_y, right_score_text.get_width(), right_score_text.get_height())
        main_display.blit(right_score_text, right_score_rect)

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

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked(pygame.mouse.get_pos())

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                reset_ball()
                game_state = "menu"

    held_keys(pygame.key.get_pressed())

    update_screen()
    clock.tick(60)

pygame.quit()
quit()
