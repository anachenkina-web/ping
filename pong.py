from pygame import *
from random import *
import time as t

window = display.set_mode((700, 500))
display.set_caption("dogonyalki")
background = transform.scale(image.load("Изображение.jpg"), (700 ,500))
font.init()
font = font.Font(None, 80)
win1 = font.render('Win', True, (255,255, 150))
win2 = font.render('Win', True, (255,255, 150))

class GameSprite(sprite.Sprite):
    def __init__(self, imageg, x, y, weidh, hight):
        super().__init__()
        self.image = transform.scale(image.load(imageg), (weidh, hight))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def __init__(self, imageg, x, y, weidh, hight, speedx, speedy):
        super().__init__(imageg, x, y, weidh, hight)
        self.speedx = speedx
        self.speedy = speedy
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy


class Player(GameSprite):
    def __init__(self, imageg, x, y, weidh, hight, speed):
        super().__init__(imageg, x, y, weidh, hight)
        self.speed = speed
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 495:
            self.rect.y += self.speed



player1 = Player("imagepryam.png" , 50, 250, 20, 100, 5)
player2 = Player("imagepryam.png" , 650, 250, 20, 100, 5)
game = True
clock = time.Clock()
ball = Ball("image.png", 250, 300, 56, 56, 3, 3) 
finish = False

while game:
    clock.tick(60)
    if not finish:
        window.blit(background, (0, 0))
        player1.reset()
        player2.reset()
        player1.update2()
        player2.update1()
        ball.reset()
        ball.update() 
        if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
            ball.speedx *= -1
        if ball.rect.y < 0 or ball.rect.y >444 :
            ball.speedy *= -1
        if ball.rect.x > 644:
            window.blit(win1, (300, 200))
            finish = True
        if ball.rect.x < 0:
            window.blit(win2, (300, 200))
            finish = True
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
