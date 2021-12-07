import pygame
from pygame.locals import *
import sys
import time
import random
import math
import pygame.freetype
from tkinter import * 
from tkinter import messagebox
import time

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Creeper Catcher")

x = 0
y = 0
height = 50
width = 50
speed = 5
score = 0
displayedPopupYet = False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.characterSprites = [pygame.image.load("assets/face1.png"),pygame.image.load("assets/face2.png")]
        self.currentFrame = 0
        self.image = self.characterSprites[self.currentFrame]
        self.rect = pygame.Rect(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,50,50)
    def update(self, pressed_keys):
        self.speed = 5
        if pressed_keys[K_LSHIFT] or pressed_keys[K_RSHIFT]:
            self.speed += 5
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
            #self.updateImage()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
            #self.updateImage()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
            #self.updateImage()
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
            #self.updateImage()
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
    # def updateImage(self):
    #     self.currentFrame += 1
    #     if self.currentFrame >= len(self.characterSprites):
    #         self.currentFrame = 0
    #     self.image = self.characterSprites[self.currentFrame]

def drawLastPost(x, y, width, height):
    pygame.draw.rect(win, (0, 0, 0), (x, y, width, height))

class defNotACreeper(pygame.sprite.Sprite):
    def __init__(self):
        super(defNotACreeper, self).__init__()
        self.surf = pygame.image.load("assets/enemy.png").convert()
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(3, 7)
        self.hardEnemy = False
        if(self.speed > 5):
            self.hardEnemy = True
            self.surf = pygame.image.load("assets/redenemy.jpg").convert()

    def update(self):
        global score 
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            if self.hardEnemy:
                score -= 1
    
    def explode(self):
        self.surf = pygame.image.load("assets/explosion.png").convert()

    def calcScore(self):
        global score
        if self.hardEnemy:
            score += 5
        else:
            score += 1
class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Score():
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None,100)
    def update(self, score):
        self.score = score
        self.scoredraw = self.font.render(("Score: " + str(self.score)), True, (255, 255, 255), (61, 109, 135))
    def draw(self):
        win.blit(self.scoredraw,(0,0))

def makePopup():
    root = Tk()
    root.geometry('471x687')
    root.title("Happy Birthday Mom!")
    root.resizable(False, False)

    bg = PhotoImage(file = "assets/momcard.png")
    label1 = Label( root, image = bg)
    label1.place(x = 0, y = 0)

    # Create Frame
    frame1 = Frame(root)
    frame1.pack(pady = 20 )
    size = 20    
    # mainMenu = Menu(root)
    # root.config(menu=mainMenu)
    # optionsMenu = Menu(mainMenu, tearoff= False)
    # mainMenu.add_cascade(label="Options", menu = optionsMenu)
    # optionsMenu.add_command(label="Restart Card", command = main())
    root.mainloop()

def main():
    global displayedPopupYet
    pygame.init()
    global score
    player = Player()
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    aGroup = pygame.sprite.Group(player)
    fpsClock = pygame.time.Clock()

    # for x in range (1000):
    #     for y in range(750):
    #         pygame.draw.rect(win, (255,255,255), rect=(0,0,64,64))
    pygame.draw.rect(win, (255,255,255), rect=(0,0,64,64))

    enemies = pygame.sprite.Group()
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 250)
    score1 = Score()
    score1.__init__

    while True:
    
        score1.update(score)
        score1.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
            elif event.type == ADDENEMY:
                new_enemy = defNotACreeper()
                enemies.add(new_enemy)
                enemies.add(new_enemy)
        pressed_keys = pygame.key.get_pressed()
        aGroup.update(pressed_keys)
        aGroup.draw(win)

        for entity in enemies:
            win.blit(entity.surf, entity.rect)
            gets_hit = pygame.sprite.spritecollide(player, enemies, True)
            if gets_hit:
                score += 1
                # entity.explode()
                if score >= 20 and not displayedPopupYet:
                    makePopup()
                    displayedPopupYet = True
            # running = False

        enemies.update()
        pygame.display.update()
        fpsClock.tick(60)
        win.fill((61, 109, 135))

if __name__ == '__main__':
    main()

