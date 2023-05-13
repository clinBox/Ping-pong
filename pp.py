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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 100, 15, 20)
        bullets.add(bullet)

window = display.set_mode((700, 500))
display.set_caption('Ping-pong')
backgraund = transform.scale(image.load('image_bg.jpg'), (700,500))

FPS = 60
clock = time.Clock()




run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.blit(backgraund,(0, 0))
    display.update()
    clock.tick(FPS)
