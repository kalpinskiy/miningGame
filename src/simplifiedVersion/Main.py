import pygame
import sys, csv

from src.simplifiedVersion.TrasureGrid import TrasureGrid
from src.simplifiedVersion.Player import Player, playerInfo
#from src.simplifiedVersion.HighScores import HighScores

pygame.init()

WIDTH = 1300
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing")
clock = pygame.time.Clock()

mine = TrasureGrid(5,7, screen)
player = Player("test", mine)
playInfo = playerInfo(player, mine)
playInfo = playerInfo(player, mine)
myNewFont = pygame.font.SysFont("Times New Roman", 25)
hsFont = pygame.font.SysFont("Times New Roman", 20)

class MyButton:
    def __init__(self, width, height, x, y, colour):
        self.font = None
        self.textColour = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.xEnd = self.x + self.width
        self.yEnd = self.y + self.height
        self.colour = colour
        self.text = None

    def hovering(self, mousePos):
        if self.xEnd >= mousePos[0] >= self.x and self.y <= mousePos[1] <= self.yEnd:
            return True
        return False

    def addText(self, text, colour, font):
        self.text = text
        self.textColour = colour
        self.font = font

    def draw(self, screen):
        buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.colour, buttonRect)
        if self.text is not None:
            buttonText = self.font.render(self.text, True, self.textColour)
            textRect = buttonText.get_rect()
            textRect.center = buttonRect.center
            screen.blit(buttonText, textRect)

class HighScores:
    def __init__(self):
        self.scores = []
        self.load()
    def load(self):
        try:
            with open("highscores.txt", "r") as f:
                #position = f.tell()
                #position = f.seek(0, 0)
                lines = csv.reader(f, delimiter=" ")
                if lines is not None:
                    m = 0
                    for line in lines:
                        m += 1
                        self.scores.append((line[0], line[1]))
                f.close()
        except FileNotFoundError:
            return

    def add_score(self, name, score):
        self.scores.append((score, name))
        self.scores.sort()
        if len(self.scores) > 10:
            self.scores.remove(self.scores[10])
    def close(self):
        my_file = open("highscores.txt", "w")
        for score in self.scores:
            my_file.write(str(score[0]) + " " + str(score[1]) + "\n")
        my_file.close()

    def draw(self, screen):
        i = 0
        x = int(screen.get_width() * 2 / 3)
        y = int(screen.get_height() - (5*20 + 4 * 4 + 2))
        for score in self.scores:
            stri = str(i) + ": " + str(score[0]) + " " + str(score[1])
            screen.blit(hsFont.render(stri, True,(0,0,0)), (x, (y + i*24)))
            i += 1
def icon(x,y):
    screen.blit(Player.playerIcon,(x,y))

def getName():
    getPlayerName = myNewFont.render("Please enter your name: ", True, (255, 255, 255))
    nameRect = getPlayerName.get_rect()
    nameRect.center = (WIDTH/2, HEIGHT/2 - 30)
    screen.blit(getPlayerName, nameRect)
    playerName = ""
    plNameRend = myNewFont.render(playerName, True, (255, 255, 255))
    plNameRect = plNameRend.get_rect()
    plNameRect.center = (WIDTH/2, HEIGHT/2 + 30)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return playerName
            elif event.key == pygame.K_BACKSPACE:
                playerName = playerName[:-1]
            elif event.key <= 127:
                playerName = playerName + chr(event.key)
                screen.blit(plNameRend, plNameRect)
                pygame.display.update()

def showHighScore():
    show = True
    while show:
        for someEvent in pygame.event.get():
            if someEvent.type == pygame.KEYDOWN:
                if someEvent.key == pygame.K_ESCAPE:
                    show = False
                    return
        screen.blit(myNewFont.render("High Scores", True, (255, 255, 255)), (100, 10))


#mine.grid[1][3] = 3
#mine.grid[2][4] = 1

#mine.print_grid()

start = False
highScore = False
helpMe = False
over = False
mainmenu = True
haveName = False
startButton = MyButton(100,50, WIDTH/2 - 50, HEIGHT/2 - 80, (255,255,255))
startButton.addText("Start [s]", (0,0,0), myNewFont)
helpButton = MyButton(100, 50, WIDTH/2 - 50, HEIGHT/2 - 25, (255,255,255))
helpButton.addText("Help [h]", (0,0,0), myNewFont)
hsButton = MyButton(100, 50, WIDTH/2 - 50, HEIGHT/2 + 30, (255,255,255))
hsButton.addText("High Scores [f]", (0,0,0), myNewFont)
highScores = HighScores()


while not over:
    while mainmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    start = True
                    mainmenu = False
                if event.key == pygame.K_h:
                    helpMe = True
                    mainmenu = False
                if event.key == pygame.K_f:
                    highScore = True
                    mainmenu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if startButton.hovering(mousePos):
                    start = True
                    mainmenu = False
                elif helpButton.hovering(mousePos):
                    helpMe = True
                    mainmenu = False
                elif hsButton.hovering(mousePos):
                    highScore = True
                    mainmenu = False
        screen.fill((122, 129, 255))
        startButton.draw(screen)
        helpButton.draw(screen)
        hsButton.draw(screen)
        pygame.display.update()
        clock.tick(60)
    while start:
        playerName = ""
        while not haveName:
            screen.fill((122, 129, 255))
            nmText = myNewFont.render("Please enter your name: ", True, (255, 255, 255))
            nameRect = nmText.get_rect()
            nameRect.center = (WIDTH/2, HEIGHT/2 - 30)
            screen.blit(nmText, nameRect)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(playerName) > 1:
                        playInfo.changeName(playerName)
                        haveName = True
                    elif event.key == pygame.K_BACKSPACE:
                        playerName = playerName[:-1]
                    elif event.key <= 127:
                        playerName += chr(event.key)
            plScreen = myNewFont.render(playerName, True, (255, 255, 255))
            plNameRect = plScreen.get_rect()
            plNameRect.center = (WIDTH/2, HEIGHT/2 + 30)
            screen.blit(plScreen, plNameRect)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.move("left")
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.move("right")
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.move("up")
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.move("down")
        if player.hits == 0:
            highScores.add_score(player.name, player.gold)
            start = False
            mainmenu = True
        screen.fill((122, 129, 255))
        mine.draw(screen)
        player.draw(screen)
        playInfo.draw(screen)
        # icon(50,50)
        pygame.display.update()
        clock.tick(60)
    while helpMe:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                helpMe = False
                mainmenu = True
        screen.fill((122, 129, 255))
        screen.blit(myNewFont.render("In this game, you are trying to find the gold coin.", True, (255, 255, 255)), (100, 10))
        screen.blit(myNewFont.render("There is only one gold coin at a time and it can generate anywhere you haven't ", True, (255, 255, 255)), (100, 20))
        pygame.display.update()
    while highScore:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                highScore = False
                mainmenu = True
        screen.fill((122, 129, 255))
        hsText = myNewFont.render("High Scores", True, (255, 255, 255))
        hsTextRect = hsText.get_rect()
        hsTextRect.center = (WIDTH / 2, 20)
        screen.blit(hsText, hsTextRect)
        highScores.draw(screen)
        pygame.display.update()

highScores.close()
screen.get_width()