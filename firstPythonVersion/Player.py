import pygame

from firstPythonVersion.MineGrid import MineGrid, MineBlock


class Player:
    playerIcon = pygame.image.load('Pictures/icons8-miner-30.png')
    def __init__(self, name, mine: MineGrid):
        self.name = name
        self.hits = 20
        self.gold = 0
        self.mine = mine
        self.x = 0
        self.y = 0

    def move(self, direction):
        block = None
        if direction == 'up' and self.y > 0:
            self.y -= 1
            block = self.mine.grid[self.y][self.x]
        elif direction == 'down' and self.y < (self.mine.numRows-1):
            self.y += 1
            block = self.mine.grid[self.y][self.x]
        elif direction == 'left' and self.x > 0:
            self.x -= 1
            block = self.mine.grid[self.y][self.x]
        elif direction == 'right' and self.x < (self.mine.numCol-1):
            self.x += 1
            block = self.mine.grid[self.y][self.x]
        if block is not None and not block.type == "empty":
            self.hits -= 1
            if block.type == "pickaxe":
                self.hits += 3
            elif block.type == "money":
                self.gold += 1
            self.mine.grid[self.y][self.x].setEmpty()
            att = [self.mine.grid[self.y][self.x]]
            self.mine.findAttainable(att)
        elif direction == 'down':
            block = self.mine.bottom[self.x]
            self.hits -= 1
            if block.type == "pickaxe":
                self.hits += 3
            elif block.type == "money":
                self.gold += 1
            self.mine.bottom[self.x].setEmpty()
            att = [self.mine.bottom[self.x]]
            self.mine.findAttainable(att)

    def draw(self, screen):
        screen.blit(self.playerIcon,((self.x * self.mine.cellSize + self.mine.x), (self.y * self.mine.cellSize + self.mine.y)))
        #infoRect = pygame.Rect(self.x, self.y, 100, 100)
        #pygame.draw.rect(screen, (255,255,255), infoRect)

class playerInfo:
    def __init__(self, player: Player, mine: MineGrid):
        self.x = mine.x + mine.numCol*mine.cellSize + 10
        self.y = mine.y + mine.numRows*mine.cellSize - 100
        self.player = player
        self.mine = mine

    def draw(self, screen):
        infoRect = pygame.Rect(self.x,self.y,100,100)
        pygame.draw.rect(screen, (255,255,255), infoRect)
        myFont = pygame.font.Font(None,20)
        goldCoins = ": " + str(self.player.gold)
        mm = myFont.render(goldCoins, True, (0,0,0))
        screen.blit(MineBlock.gold,(self.x, self.y))
        screen.blit(mm,(self.x + 25, self.y+2))
        screen.blit(MineBlock.pickaxe, (self.x, self.y+30))
        hitss = ": " + str(self.player.hits)
        nn = myFont.render(hitss, True, (0,0,0))
        screen.blit(nn,(self.x+25, self.y+32))