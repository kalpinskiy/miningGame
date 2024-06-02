import random
import pygame


class MineBlock:
    def __init__(self, x, y, mine):
        self.mine = mine
        self.size = 30
        v = random.randint(0, 19)
        self.x = x
        self.xCoord = self.mine.x + self.size * self.x
        self.y = y
        self.yCoord = self.mine.y + self.size * self.y
        if v < 11:
            self.type = "dirt"
            self.color = (125, 105, 77)
        elif v < 16:
            self.type = "empty"
            self.color = (79, 101, 136)
        elif v < 19:
            self.type = "money"
            self.color = (125, 105, 77)
        elif v < 20:
            self.type = "pickaxe"
            self.color = (125, 105, 77)
        self.attainable = False

    def setAttainable(self):
        self.attainable = True
        if self.type == "empty":
            self.color = (122, 129, 255)
        else:
            self.color = (159, 133, 98)

    def setEmpty(self):
        self.type = "empty"
        self.color = (122, 129, 255)

    gold = pygame.image.load('Pictures/icons8-coin-20.png')
    pickaxe = pygame.image.load('Pictures/icons8-pickaxe-20-1.png')

    def showGold(self, screen):
        screen.blit(self.gold, (self.xCoord + 5, self.yCoord + 5))

    def showPickaxe(self, screen):
        screen.blit(self.pickaxe, (self.xCoord + 5, self.yCoord + 5))

    def draw(self, screen):
        cellRect = (self.xCoord + 1, self.yCoord + 1, self.size - 1, self.size - 1)
        pygame.draw.rect(screen, self.color, cellRect)
        if self.type == "money":
            self.showGold(screen)
        elif self.type == "pickaxe":
            self.showPickaxe(screen)


class MineGrid:
    def __init__(self):
        self.numRows = 7
        self.numCol = 5
        self.cellSize = 30
        self.x = 50
        self.y = 50
        self.head = [MineBlock(i, -1, self) for i in range(self.numCol)]
        for block in self.head:
            block.setAttainable()
        self.grid = [[MineBlock(j, i, self) for j in range(self.numCol)] for i in range(self.numRows)]
        self.bottom = [MineBlock(i, self.numRows, self) for i in range(self.numCol)]
        self.grid[0][0].setEmpty()
        att = [self.grid[0][0]]
        self.findAttainable(att)
        self.xEnd = self.x + self.numCol * self.cellSize
        self.yEnd = self.y + self.numRows * self.cellSize

    def findAttainable(self, att):
        for block in att:
            if block.y < (self.numRows - 1):
                if not block.attainable:
                    block.setAttainable()
                    if block.type == "empty":
                        att.append(block)
            elif block.y == (self.numRows - 1):
                if not self.bottom[block.x].attainable:
                    self.bottom[block.x].setAttainable()
                    if self.bottom[block.x].type == "empty":
                        att = self.addLevel(self.bottom[block.x], att)
                        block.y -= 1
            else:
                att = self.addLevel(self.bottom[block.x], att)
                block.y -= 1
            if block.y != 0:
                if not self.grid[block.y - 1][block.x].attainable:
                    self.grid[block.y - 1][block.x].setAttainable()
                    if self.grid[block.y - 1][block.x].type == "empty":
                        att.append(self.grid[block.y - 1][block.x])
            if block.x != 0:
                if not self.grid[block.y][block.x - 1].attainable:
                    self.grid[block.y][block.x - 1].setAttainable()
                    if self.grid[block.y][block.x - 1].type == "empty":
                        att.append(self.grid[block.y][block.x - 1])
            if block.x != (self.numCol - 1):
                if not self.grid[block.y][block.x + 1].attainable:
                    self.grid[block.y][block.x + 1].setAttainable()
                    if self.grid[block.y][block.x + 1].type == "empty":
                        att.append(self.grid[block.y][block.x + 1])

    def addLevel(self, xhit, att):
        self.head = self.grid[0]
        for l in range(self.numRows - 1):
            self.grid[l] = self.grid[l + 1]
        self.grid[self.numRows - 1] = self.bottom
        self.bottom = [MineBlock(a, self.numRows, self) for a in range(self.numCol)]
        self.bottom[xhit].setAttainable()
        if self.bottom[xhit].type == "empty":
            att.append(self.bottom[xhit])
        return att

    def print_grid(self):
        for row in range(self.numRows):
            for column in range(self.numCol):
                print(self.grid[row][column], end=" ")
            print()

    def draw(self, screen):
        for row in range(self.numRows):
            for coll in range(len(self.grid[row])):
                self.grid[row][coll].draw(screen)
        pygame.draw.line(screen, (0, 0, 0), (self.x + 1, self.yEnd), (self.xEnd - 1, self.yEnd), 2)
        for bl in range(self.numCol):
            self.bottom[bl].draw(screen)