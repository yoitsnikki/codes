'''
Nikki Agrawal
Pygame Coding Game

Coding a ball and paddle game where you bounce the ball off of the paddle.

Using instructions from the Python for Kids Book
'''

import pygame, sys
from pygame.locals import *

x = 0

#This class will define properties and behavior for the ball
class Ball:
    def __init__(self, paramColor, paramRadius, paramScreen, paramSpeedX, paramSpeedY):
        self.color = paramColor
        self.radius = paramRadius
        self.speed_x = paramSpeedX
        self.speed_y = paramSpeedY
        self.x = 200
        self.y = 150
        self.screen = paramScreen

    def draw(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y

    if (self.x > screen.get_width() or self.x < 0):
        self.speed_x = self.speed_x * -1

    if (self.y > screen.get_height() or self.y < 0):
        self.speed_y = self.speed_y * -1

    pygame.draw.circle(self.screen, self.color, [self.x, self.y], self.radius, 0)

    def checkPaddleHit (self, paddle):
        #Check if the ball hit the paddle
        ball_x1 = self.radius-self.x
        ball_x2 = self.radius+self.y
        ball_y1 = self.y-self.radius
        ball_y2 = self.y+self.radius

        paddle_x1 = paddle.x
        paddle_x2 = paddle.x+paddle.width
        paddle_y1 = paddle.y
        paddle_y2 = paddle.y+paddle.height

    if (ball_x2 > paddle_x1 and ball_x1 < paddle_x2) and (ball_y2 > paddle_y1 and ball_y1 < paddle_y2):
        self.speed_y = -self.speed_y
        paddle.score += 1

#Creates the paddle and keeps track of it
class Paddle:
    def __init__(self, color, width, height, screen):
        self.screen = screen
        self.color = color
        self.width = width
        self.height = height
        self.x = 200
        self.y = 250
        self.score = 0

    def updateXCoord (self, mouseXPos):
        self.x = mouseXPos

    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height], 0)

pygame.init()
pygame.font.init()

#Define a font
myfont = pygame.font.SysFont('Arial', 25)

screen = pygame.display.set_mode([400, 300])
pygame.display.set_caption('Pong Game')

RED = [255, 0, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
PURPLE = [204, 102, 255]

print("Ready?")
print("Set?")
print("GO!")

#instantiate the ball
ball = Ball(RED, 10, screen, 15, -15)
ball2 = Ball(BLACK, 15, screen, 20, -20)

#insastantiate the paddle
paddle =Paddle(PURPLE, 80, 20, screen)

#Insastantiate the score
score = 0

while True:
    for event in pygame.event.get():
        if (event.type == QUIT):
            pygame.quit()
            sys.exit()

        elif (event.type == pygame.MOUSEMOTION):
            paddle.updateXCoord (pygame.mouse.get_pos()[0])

screen.fill(WHITE)
pygame.time.delay(20)

ball.draw()
ball2.draw()
paddle.draw()
ball.checkPaddleHit(paddle)
ball2.checkPaddleHit(paddle)

label = myfont.render('Score: ' + str(paddle.score), True, (0,0,128), (255,255,255))

screen.blit(label, (40,15))
pygame.display.update()
