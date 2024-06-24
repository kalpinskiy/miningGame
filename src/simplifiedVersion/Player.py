import pygame

from src.simplifiedVersion.TrasureGrid import TrasureGrid
from pathlib import Path
import math

fibonacci = [1,1]
while fibonacci[len(fibonacci) - 1] < 101:
    fibonacci.append(fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2])

class Player:
    icon_path = Path(__file__).resolve().parent.parent / 'firstPythonVersion' / 'Pictures' / 'icons8-miner-30.png'
    playerIcon = pygame.image.load(icon_path)
    def __init__(self, name, mine: TrasureGrid):
        self.name = name
        self.hits = 20
        self.gold = 0
        self.mine = mine
        self.x = 0
        self.y = 0
        self.direction = None
        self.distance = None
        self.dirRad = None
        self.updateDist()

    def updateDist(self):
        self.distance = (abs(self.x - self.mine.goalCell[0]) + abs(self.y - self.mine.goalCell[1]))
        dire = math.degrees(math.atan2(self.mine.goalCell[1] - self.y, self.mine.goalCell[0] - self.x))
        self.dirRad = math.degrees(math.atan2(self.mine.goalCell[1] - self.y, self.mine.goalCell[0] - self.x))
        if dire >= 22.5 and dire < (45+22.5):
            self.direction = 45
        elif dire >= (45 + 22.5) and dire < (90 + 22.5):
            self.direction = 90
        elif dire >= (90 + 22.5) and dire < (135 + 22.5):
            self.direction = 135
        elif dire >= (135 + 22.5) or dire < -(135 + 22.5):
            self.direction = 180
        elif dire < 22.5 and dire >= -22.5:
            self.direction = 0
        elif dire < -22.5 and dire >= -(45 + 22.5):
            self.direction = 315
        elif dire < -(45 + 22.5) and dire >= -(90 + 22.5):
            self.direction = 270
        else:
            self.direction = 225

    def changeName(self, newName: str):
        self.name = newName

    def move(self, direction):
        block = None
        if direction == 'up' and self.y < self.mine.maxY:
            self.y += 1
            block = (self.x, self.y)
        elif direction == 'down' and self.y > (self.mine.maxY * -1):
            self.y -= 1
            block = (self.x, self.y)
        elif direction == 'left' and self.x > (self.mine.maxX * -1):
            self.x -= 1
            block = (self.x, self.y)
        elif direction == 'right' and self.x < self.mine.maxX:
            self.x += 1
            block = (self.x, self.y)
        self.updateDist()
        if self.distance == 0:
            self.hits -= 1
            self.gold += 1
            self.mine.grid[block] = 1
            if self.gold in fibonacci:
                self.mine.addLevel()
            self.mine.setGoal()
            self.updateDist()
        else:
            if block is not None and self.mine.grid[block] != 1:
                self.hits -= 1
                if block == 4:
                    self.hits += 3
                self.mine.grid[block] = 1
                att = [(self.x, self.y)]
                self.mine.findVisibility(att)

    def draw(self, screen):
        screen.blit(self.playerIcon, (self.x * self.mine.cellSize + self.mine.x, (self.y * self.mine.cellSize) * -1 +
                                                                                   self.mine.y))
        #infoRect = pygame.Rect(self.x, self.y, 100, 100)
        #pygame.draw.rect(screen, (255,255,255), infoRect)

class playerInfo:
    dir0 = pygame.image.load(Path(__file__).resolve().parent / 'pics' / 'icons8-circled-right-25.png')
    dir45 = pygame.image.load(Path(__file__).resolve().parent / 'pics' / 'icons8-circled-up-right-25.png')
    dir90 = pygame.image.load(Path(__file__).resolve().parent / 'pics' / 'icons8-upward-arrow-25.png')
    dir135 = pygame.image.load(Path(__file__).resolve().parent / 'pics' / 'icons8-circled-up-left-25.png')
    dir180 = pygame.image.load(Path(__file__).resolve().parent / 'pics' / 'icons8-go-back-25.png')
    dir225 = pygame.image.load(Path(__file__).resolve().parent / 'pics' / 'icons8-circled-down-left-25.png')
    dir270 = pygame.image.load(Path(__file__).resolve().parent / 'pics' / 'icons8-below-25.png')
    dir315 = pygame.image.load(Path(__file__).resolve().parent / 'pics' / 'icons8-circled-down-right-25.png')
    def __init__(self, player: Player, mine: TrasureGrid):
        self.height = 150
        self.width = 100
        self.x = mine.x + mine.cellSize * (mine.numCols / 2 + 10) + 50
        self.y = mine.y - self.height / 2
        self.player = player
        self.mine = mine

    def draw(self, screen):
        infoRect = pygame.Rect(self.x,self.y,100,150)
        pygame.draw.rect(screen, (255,255,255), infoRect)
        myFont = pygame.font.SysFont("Times New Roman",20)
        plname = myFont.render(str(self.player.name), True, (255,255,255))
        plnamerect = plname.get_rect()
        plnamerect.center = (self.x + self.width / 2, self.y + self.height / 2)
        screen.blit(plname, plnamerect)
        goldCoins = ": " + str(self.player.gold)
        mm = myFont.render(goldCoins, True, (0,0,0))
        screen.blit(TrasureGrid.gold, (self.x, self.y + 30))
        screen.blit(mm,(self.x + 25, self.y+32))
        screen.blit(TrasureGrid.pickaxe, (self.x, self.y + 60))
        hitss = ": " + str(self.player.hits)
        nn = myFont.render(hitss, True, (0,0,0))
        screen.blit(nn,(self.x+25, self.y+62))
        screen.blit((myFont.render("Distance: " + str(self.player.distance), True, (0,0,0))),(self.x+25, self.y+92))
        match self.player.direction:
            case 0:
                screen.blit(self.dir0, (self.x, self.y + 92))
            case 45:
                screen.blit(self.dir45,(self.x, self.y + 92))
            case 90:
                screen.blit(self.dir90,(self.x, self.y + 92))
            case 135:
                screen.blit(self.dir135,(self.x, self.y + 92))
            case 180:
                screen.blit(self.dir180,(self.x, self.y + 92))
            case 225:
                screen.blit(self.dir225,(self.x, self.y + 92))
            case 270:
                screen.blit(self.dir270,(self.x, self.y + 92))
            case 315:
                screen.blit(self.dir315,(self.x, self.y + 92))

    def changeName(self, newName: str):
        self.player.changeName(newName)