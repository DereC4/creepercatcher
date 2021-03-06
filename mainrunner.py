import pygame
from pygame.locals import *
import random
import pygame.freetype
import tkinter
from tkinter import * 
from tkinter import messagebox
import time

SCREEN_WIDTH = 600
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
displayedPopupYet2 = False
displayedPopupYet3 = False
totalscore = 0

# with open("scores.txt", "r", encoding="utf-16") as file:
#     scores = file.readlines()
# highscore = scores[0].replace("highscore: ","")
# print(int(scores[0]))
# highscore = int(scores[0])
# print(int(highscore))

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
        global score
        super(defNotACreeper, self).__init__()
        self.surf = pygame.image.load("assets/enemy.png").convert()
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(SCREEN_HEIGHT/2+100,SCREEN_HEIGHT-10),
            ) 
        )
        if score > 20:
            self.speed = random.randint(score-18, score-10)
        else:
            self.speed = random.randint(3, 7)
        self.difficulty = "normal"
        if(self.speed > 5):
            self.difficulty = "hard"
            self.surf = pygame.image.load("assets/redenemy.jpg").convert()
        if(self.speed > 15):
            self.difficulty = "super hard"
            self.surf = pygame.image.load("assets/stoneblueenemy.jpg").convert()

    def update(self):
        global score 
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            if self.difficulty=='hard':
                score -= 1
            if self.difficulty=="super hard":
                score -= 2
    
    def explode(self):
        self.surf = pygame.image.load("assets/explosion.png").convert()

    def calcScore(self):
        global score
        if self.difficulty=="hard":
            score += 1
        else:
            score += 1
    
    def getDifficulty(self):
        return self.difficulty

class Score():
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None,50)
    def update(self, score):
        self.score = score
        self.scoredraw = self.font.render(("Score: " + str(self.score)), True, (255, 255, 255), (61, 109, 135))
    def draw(self):
        global totalscore
        win.blit(self.scoredraw,(0,SCREEN_HEIGHT-30))
        if(self.score>totalscore):
            totalscore = self.score
        # if(self.score>highscore):
        #     file = open("scores.txt","r+")
        #     file.truncate(0)
        #     file.write(str(self.score))
        #     highscore = self.score()
        #     file.close()

class Background():
    def __init__(self):
        self.bgimage = pygame.image.load('assets/tempbackground.png')
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = -50
        self.bgX1 = 0

        self.bgY2 = -50
        self.bgX2 = self.rectBGimg.width

        self.moving_speed = 5
        
    def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width
            
    def render(self):
        win.blit(self.bgimage, (self.bgX1, self.bgY1))
        win.blit(self.bgimage, (self.bgX2, self.bgY2))

class Background2():
    def __init__(self):
        self.bgimage = pygame.image.load('assets/tempbackground.jpg')
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 290
        self.bgX1 = 0

        self.bgY2 = 290
        self.bgX2 = self.rectBGimg.width

        self.moving_speed = 5
        
    def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width
            
    def render(self):
        win.blit(self.bgimage, (self.bgX1, self.bgY1))
        win.blit(self.bgimage, (self.bgX2, self.bgY2))
        
def resetGame():
    global score, totalscore, displayedPopupYet, displayedPopupYet2, displayedPopupYet3
    displayedPopupYet = False
    displayedPopupYet2 = False
    displayedPopupYet3 = False
    score = 0
    totalscore = 0
def makePopup():
    global score 
    root = Tk()
    root.geometry('471x687')
    root.resizable(False, False)
    bg = PhotoImage(file = "assets/face1.png")

    if (score > 19):
        root.title("20 points!")
        bg = PhotoImage(file = "assets/explosion.png")

    if (score >= 40):
        root.title("Victory!!!")
        root.geometry('852x480')
        bg = PhotoImage(file = "assets/youwin.png")
        # B = tkinter.Button(root, text ="Reset this world", command = resetGame())
        # B.pack()

    if (score >= 61):
        root.title("Victory!!!")
        root.geometry('1280x720')
        bg = PhotoImage(file = "assets/secretending.png")

    label1 = Label( root, image = bg)
    label1.place(x = 0, y = 0)

    # Create Frame
    frame1 = Frame(root)
    frame1.pack(pady = 20 )

    root.mainloop()

def main():
    global displayedPopupYet, displayedPopupYet2, displayedPopupYet3
    pygame.init()
    global score, totalscore
    player = Player()
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    aGroup = pygame.sprite.Group(player)
    fpsClock = pygame.time.Clock()
    background = Background()
    background2 = Background2()
    # for x in range (1000):
    #     for y in range(750):
    #         pygame.draw.rect(win, (255,255,255), rect=(0,0,64,64))
    pygame.draw.rect(win, (255,255,255), rect=(0,0,64,64))

    enemies = pygame.sprite.Group()
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 250)
    score1 = Score()

    while True:
        if score >= 21 and not displayedPopupYet:
            makePopup()
            displayedPopupYet = True
        if score >= 40 and not displayedPopupYet2:
            makePopup()
            displayedPopupYet2 = True
        if score >= 61 and not displayedPopupYet3:
            makePopup()
            displayedPopupYet3 = True

        background.update()
        background.render()
        background2.update()
        background2.render()
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
                # print(entity.getDifficulty())
                if(entity.getDifficulty()=="hard"):
                    score += 1
                elif(entity.getDifficulty()=="super hard"):
                    score += 2
                # entity.explode()

        enemies.update()
        pygame.display.update()
        fpsClock.tick(60)
        win.fill((61, 109, 135))

if __name__ == '__main__':
    main()

