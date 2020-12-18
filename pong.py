import pygame
import random
pygame.init()
# print(pygame.font.get_fonts())
# a = input()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("pong game")
clock = pygame.time.Clock()
bg_color = (200,200,200)
color = (70,70,70)
slab_height = 100
slab_width =  10
player = pygame.Rect(-10+screen_width-slab_width,screen_height/2-slab_height/2,slab_width,slab_height)
opponent = pygame.Rect(0+10,screen_height/2-slab_height/2,slab_width,slab_height)
ball = pygame.Rect(screen_width/2-15,screen_height/2-15,25,25)
ball_vel_x=5
ball_vel_y=5
player_vel = 0
opponent_vel = 4
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)
score_timer = True
game_loop = True
def draw():
    screen.fill(bg_color)
    player_score_text = game_font.render(str(player_score),True,pygame.Color('Red'))
    opponet_score_text = game_font.render(str(opponent_score),True,pygame.Color('Red'))
    screen.blit(player_score_text,(screen_width/2+20,screen_height/2-player_score_text.get_height()/2))
    screen.blit(opponet_score_text,(screen_width/2-20-opponet_score_text.get_width(),screen_height/2-opponet_score_text.get_height()/2))
    pygame.draw.aaline(screen,color,(screen_width/2,0),(screen_width/2,screen_height))
    pygame.draw.rect(screen,color,player)
    pygame.draw.rect(screen,color,opponent)
    pygame.draw.ellipse(screen,color,ball)
def ball_restart():
    global ball_vel_x,ball_vel_y,score_timer
    ball.center = (screen_width/2,screen_height/2)
    current_time = pygame.time.get_ticks()
    if current_time - score_timer < 2100:
        timer_value = current_time - score_timer
        if 0<= timer_value <  700:
            timer_value = 3
        elif 700<=timer_value <1400:
            timer_value = 2
        elif 1400<=timer_value<2100:
            timer_value = 1
        timer_text = game_font.render(str(timer_value),True,pygame.Color("RED"))
        screen.blit(timer_text,(screen_width/2-timer_text.get_width()/2,screen_height/2+20))
        ball_vel_x = 0
        ball_vel_y = 0
    else:
        ball_vel_x = 5 * random.choice((1,-1))
        ball_vel_y = 5 * random.choice((1,-1))
        score_timer = None
def ball_animation():
    global ball_vel_x,ball_vel_y,player_score,opponent_score,score_timer
    if ball.left<=0:
        player_score+=1
        score_timer = pygame.time.get_ticks()
    if ball.right>=screen_width:
        opponent_score+=1
        score_timer = pygame.time.get_ticks()
    if ball.top<=0 or ball.bottom>=screen_height:
        ball_vel_y*=-1
    ball.x+=ball_vel_x
    ball.y+=ball_vel_y
def player_animation():
    player.y+=player_vel
    if player.top<=0 :
        player.top = 0
    if player.bottom>=screen_height:
        player.bottom = screen_height
def opponent_animation():
    if ball.y>=opponent.bottom:
        opponent.y+=opponent_vel
    if ball.y<=opponent.top:
        opponent.y-=opponent_vel
def collision_check(ball,slab):
    global ball_vel_x,ball_vel_y
    if not ball.colliderect(slab):
        return
    if abs(ball.left-slab.right)<10 or abs(ball.right-slab.left)<10:
        ball_vel_x*=-1
    elif abs(ball.top-slab.bottom)<10 or abs(ball.bottom-slab.top)<10:
        ball_vel_y*=-1
while(game_loop):
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            game_loop = False
    keys = pygame.key.get_pressed()
    player_vel = 0
    if keys[pygame.K_DOWN]:
        player_vel += 7
    if keys[pygame.K_UP]:
        player_vel += -7
    draw()
    if score_timer!=None:
        ball_restart()
    ball_animation()
    player_animation()
    opponent_animation()
    pygame.display.update()
    # if ball.colliderect(player) or ball.colliderect(opponent):
    #     ball_vel_x*=-1
    collision_check(ball,player)
    collision_check(ball,opponent)
    clock.tick(60)
pygame.quit()