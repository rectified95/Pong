import pygame, sys, time, COMMONS, os, random
import copy
from Ball import Ball
import math
from Paddle import Paddle
from pygame.locals import *

def run(disk_hole):

    pygame.init()
    pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
    r             = 0
    center        = [COMMONS.WINDOWWIDTH/2, COMMONS.WINDOWHEIGHT/2]
    radius        = 15
    ball_vels     = [[3,1], [2,1], [-3,1], [3,-1], [-3,-1], [-2,-2], [-2,1]]
    ball_vel      = random.choice(ball_vels)
    win_banner_pos = {'left': [100, 50], 'right': [458, 50]}
    paddle_speed  = 7
    paddle_height = 100
    paddle_width  = 10
    ball          = Ball(center, radius, ball_vel, COMMONS.REDDISH)
    paddle_1      = Paddle(0, 150, paddle_width, paddle_height, COMMONS.BLUEISH, paddle_speed, ball)
    paddle_2      = Paddle(COMMONS.WINDOWWIDTH - paddle_width, 150, paddle_width, paddle_height, COMMONS.BLUEISH, paddle_speed, ball)
    dirty_rectangles = [ball.get_rect(), paddle_1.get_rect(), paddle_2.get_rect()]
    score_Font = pygame.font.SysFont("Verdana", 35)
    spaces = "                            " # dirty hack to display both scores at once (to avoid double blitting the score Font objects)
    windowSurface = pygame.display.set_mode((COMMONS.WINDOWWIDTH, COMMONS.WINDOWHEIGHT), DOUBLEBUF, 32)
    pygame.display.set_caption('Pong')
    pygame.draw.circle(windowSurface, ball.color, (ball.x, ball.y), ball.radius)
    pygame.draw.circle(windowSurface, COMMONS.WHITE, (ball.x, ball.y), ball.radius + 2, ball.radius - disk_hole)
    pygame.display.update()
    time.sleep(1)        
    #mainCLock 	  = pygame.time.Clock()

    ball_copy 	  = copy.deepcopy(ball)
    scoreLeft 	  = scoreRight = 0

    while max(scoreLeft, scoreRight) < 3:
        in_game = True
        paddle_1_down = paddle_1_up = paddle_2_down = paddle_2_up = False
        mainCLock     = pygame.time.Clock()
        
        while in_game == True:
            for event in pygame.event.get():
                
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        paddle_2_down = True
                    elif event.key == K_UP:
                        paddle_2_up = True
                    elif event.key == ord('s'):
                        paddle_1_down = True
                    elif event.key == ord('w'):
                        paddle_1_up = True
                    elif event.key == ord('r'):
                        scoreRight = scoreLeft = 0
                        ball.x = COMMONS.WINDOWWIDTH/2
                        ball.y = COMMONS.WINDOWHEIGHT/2
                        ball.vel  =random.choice(ball_vels)
                    elif event.key == ord('q'):
                        pygame.quit()
                        sys.exit()

                elif event.type == KEYUP:
                    if event.key == K_DOWN:
                        paddle_2_down = False
                    elif event.key == K_UP:
                        paddle_2_up = False
                    elif event.key == ord('s'):
                        paddle_1_down = False
                    elif event.key == ord('w'):
                        paddle_1_up = False
                
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
            if paddle_1_down:
                paddle_1.move(1)
            elif paddle_1_up:
                paddle_1.move(-1)
            elif paddle_2_down:
                paddle_2.move(1)
            elif paddle_2_up:
                paddle_2.move(-1)
                
            ball.check_board_bounce() 
            ball.move()   
            
            if ball.x - ball.radius <= 0: 
                if ball.y >= paddle_1.y and ball.y <= paddle_1.y + paddle_1.height:
                    ball.vel[0] = -int(math.floor(1.1*ball.vel[0]))
                    print ball.vel[0]
                else:
                    scoreRight += 1
                    in_game = False
                    
                    
            elif ball.x + ball.radius >= COMMONS.WINDOWWIDTH:
                if ball.y >= paddle_2.y and ball.y <= paddle_2.y + paddle_2.height:
                    ball.vel[0] = int(math.floor(-1.1*ball.vel[0]))
                    print ball.vel[0]
                else:
                    scoreLeft += 1
                    in_game = False
                    
                                
            windowSurface.fill(COMMONS.BLACK)
            

            windowSurface.lock()

            pygame.draw.line(windowSurface, COMMONS.WHITE, (COMMONS.WINDOWWIDTH/2, 0), (COMMONS.WINDOWWIDTH/2, COMMONS.WINDOWHEIGHT), 2)
            pygame.draw.line(windowSurface, COMMONS.WHITE, (paddle_1.width, 0), (paddle_1.width, COMMONS.WINDOWHEIGHT), 1)
            pygame.draw.line(windowSurface, COMMONS.WHITE, (COMMONS.WINDOWWIDTH - paddle_2.width, 0), (COMMONS.WINDOWWIDTH - paddle_2.width, COMMONS.WINDOWHEIGHT), 1)
            
            pygame.draw.circle(windowSurface, ball.color, (ball.x, ball.y), ball.radius)
            pygame.draw.circle(windowSurface, COMMONS.WHITE, (ball.x, ball.y), ball.radius + 2, ball.radius - disk_hole)
            
            pygame.draw.rect(windowSurface, paddle_1.color, pygame.Rect(paddle_1.x, paddle_1.y, paddle_1.width, paddle_1.height))
            pygame.draw.rect(windowSurface, paddle_2.color, pygame.Rect(paddle_2.x, paddle_2.y, paddle_2.width, paddle_2.height))
            
            windowSurface.unlock()

            scoreSurface = score_Font.render(str(scoreLeft)+spaces+str(scoreRight), False, COMMONS.WHITE)
            windowSurface.blit(scoreSurface, (150,80))
           
            pygame.display.update()
            #mainCLock.tick_busy_loop(100)
            mainCLock.tick(100)
        #time.sleep(0.5)
        
        #ball = copy.deepcopy(ball_copy)
        ball.x = ball_copy.x
        ball.y = ball_copy.y
        ball.vel = random.choice(ball_vels)
        pygame.time.wait(500)

    win_Surface = pygame.font.SysFont("Verdana", 30).render("You win", False, COMMONS.WHITE)
    if scoreLeft > scoreRight:
        winner = 'left' 
    else:
        winner = 'right'
    windowSurface.blit(win_Surface, win_banner_pos[winner])
    pygame.display.update()     
 

def super_run(disk_hole):

    run(disk_hole)
    while True:
        for event in pygame.event.get():  
            if event.type == KEYDOWN:
                if event.key == ord('r'):
                    run(disk_hole)
                elif event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
        time.sleep(1)


def main():

    disk_hole     = 10
    super_run(disk_hole)
    os.system("pause")
    pygame.quit()
    return 0
    

if __name__ == "__main__":
    main()

    #POSSIBLE OPTIMIZATION: USE 'DIRTY RECTANGLE DISPLAY UPDATING'
    # ADD 'GAME' CLASS