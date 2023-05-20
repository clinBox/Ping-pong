from pygame import *
from random import *
from time import time as timer 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed


window = display.set_mode((700, 500))
display.set_caption('Ping-pong')
backgraund = transform.scale(image.load('2.jpg'), (700,500))

speed_x = 3
speed_y = 3


rocket2 = Player('1.png',30,30,4, 20, 100)
rocket1 = Player('1.png',650, 30, 4, 20, 100 )
ball = GameSprite('5.jpg', 200, 200, 4, 65, 50)


FPS = 60
clock = time.Clock()

font.init()
font = font.SysFont('Arial', 80)

lose1 = font.render('Player 1 lose', True, (255,0,0))
lose2 = font.render('Player 2 lose', True, (255,0,0))

run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.blit(backgraund,(0, 0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y  <0 or ball.rect.y  >450:
            speed_y *=- 1
        if sprite.collide_rect(rocket1,ball) or sprite.collide_rect(rocket2,ball):
            speed_x *=- 1
        if ball.rect.x <0:
            finish = True
            window.blit(lose1,(200,200))
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2,(200,200))

        rocket1.update1()
        rocket2.update2()
        rocket1.reset()
        rocket2.reset()
        ball.reset()
       




    display.update()
    clock.tick(FPS)