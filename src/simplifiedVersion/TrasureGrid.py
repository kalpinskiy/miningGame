import random
import pygame

from pathlib import Path
from collections import defaultdict


"""
0 dirt
1 empty visible
2 empty not visible
3 coin
4 pickax
"""


class TrasureGrid:
    pictures_path = Path(__file__).resolve().parent.parent / 'firstPythonVersion' / 'Pictures'
    gold_path = pictures_path / 'icons8-coin-20.png'
    pickaxe_path = pictures_path / 'icons8-pickaxe-20-1.png'
    gold = pygame.image.load(gold_path)
    pickaxe = pygame.image.load(pickaxe_path)
    #icons8-pickaxe-20-1.png
    empty = (122,129,255)
    emptyNA = (79,101,136)
    general = (159,133,98)
    generalNA = (125,105,77)

    def showGold(self,screen,x,y):
        screen.blit(self.gold,(x,y))
    def showPickaxe(self,screen,x,y):
        screen.blit(self.pickaxe,(x,y))

    def assignRandom(self):
        """Used to randomly generate a value for each mine block.
        Odd values are given to all, meaning the blocks are initially non-visible.
        @:return value of 1 means an empty cell
        @:return value of 3 means dirt
        @:return value of 5 means pickaxe
        @:return value of 7 means money"""
        val = random.randint(0,19)
        if val < 11:
            return 3
        elif val < 16:
            return 1
        elif val < 19:
            return 7
        elif val < 20:
            return 5

    def setGoal(self):
        valX = random.randint((self.maxX * -1), self.maxX)
        valY = random.randint((self.maxY * -1), self.maxY)
        if self.grid[(valX, valY)] == 0:
            self.grid[(valX, valY)] = 3
            self.goalCell = (valX, valY)
        else:
            self.setGoal()

    def addPickaxe(self):
        valX = random.randint((self.maxX * -1), self.maxX)
        valY = random.randint((self.maxY * -1), self.maxY)
        if self.grid[(valX, valY)] == 0:
            self.grid[(valX, valY)] = 4
            self.picks.append((valX, valY))
            return valX, valY
        else:
            self.addPickaxe()

    def findVisibility(self, att):
        for block in att:
            #left
            if block[0] > (self.maxX * -1):
                if self.grid[(block[0] - 1, block[1])] == 2:
                    self.grid[(block[0] - 1, block[1])] = 1
                    att.append((block[0] - 1, block[1]))
            #set right
            if block[0] < self.maxX:
                if self.grid[(block[0] + 1, block[1])] == 2:
                    self.grid[(block[0] + 1, block[1])] = 1
                    att.append((block[0] + 1, block[1]))
            if block[1] < self.maxY:
                if self.grid[(block[0], block[1] + 1)] == 2:
                    self.grid[(block[0], block[1] + 1)] = 1
                    att.append((block[0], block[1] + 1))
            if block[1] > (self.maxY * -1):
                if self.grid[(block[0], block[1] - 1)] == 2:
                    self.grid[(block[0], block[1] - 1)] = 1
                    att.append((block[0], block[1] - 1))

    def __init__(self, rows, cols, screen):
        self.numRows = rows
        self.numCols = cols
        self.maxX = int((self.numCols - 1) /2)
        self.maxY = int((self.numRows - 1) /2)
        self.cellSize = 30
        screenwidth, screenheight = screen.get_size()
        self.x = screenwidth / 2 - 50
        self.y = screenheight / 2
        self.grid = defaultdict(int)
        self.grid[(0, 0)] = 1
        for i in range(0, int(self.numRows * self.numCols /4)):
            valX = random.randint(self.maxX * -1, self.maxX)
            valY = random.randint(self.maxY * -1, self.maxY)
            while self.grid[(valX, valY)] != 0:
                valX = random.randint(self.maxX * -1, self.maxX)
                valY = random.randint(self.maxY * -1, self.maxY)
            self.grid[(valX, valY)] = 2
        att = [(0, 0)]
        self.findVisibility(att)
        self.goalCell = (0, 0)
        self.setGoal()
        self.picks = []

    def addLevel(self):
        self.numCols += 2
        self.numRows += 2
        self.maxX += 1
        self.maxY += 1
        for i in range(int((self.numRows * 2 + self.numCols * 2 - 4) / 4) + 1):
            valR = random.randint(0, 3)
            if valR == 0 or valR == 1:
                neg = -1 ** valR
                valM = random.randint(self.maxX * -1, self.maxX)
                while self.grid[(valM, self.maxY * neg)] == 2:
                    valM = random.randint(self.maxX * -1, self.maxX)
                if self.grid[(valM, (self.maxY -1) * neg)] == 1:
                    self.grid[(valM, self.maxY * neg)] = 1
                else:
                    self.grid[(valM, self.maxY * neg)] = 2
            else:
                neg = -1 ** valR
                valM = random.randint(self.maxY * -1, self.maxY)
                while self.grid[(self.maxX * neg, valM)] == 2:
                    valM = random.randint(self.maxY * -1, self.maxY)
                if self.grid[((self.maxX -1) * neg, valM)] == 1:
                    self.grid[(self.maxX * neg, valM)] = 1
                else:
                    self.grid[(self.maxX * neg, valM)] = 2
    def print_grid(self):
        for row in range(self.numRows):
            for column in range(self.numCol):
                print(self.grid[row][column], end = " ")
            print()

    def draw(self, screen):
        for currentY in range((self.maxY * -1), self.maxY +1):
            for currentX in range((self.maxX * -1), self.maxX +1):
                if self.grid[(currentX, currentY)] != 1:
                    myColor = self.general
                    cellRect = pygame.Rect(self.x + currentX * self.cellSize +1, self.y + currentY*self.cellSize *-1 + 1, self.cellSize-1, self.cellSize-1)
                    pygame.draw.rect(screen, myColor, cellRect)
                    """if self.grid[row][coll] == 4 or self.grid[row][coll] == 5:
                        self.showPickaxe(screen,self.x + coll * self.cellSize+5, self.y + row*self.cellSize+5)
                    elif self.grid[row][coll] == 6 or self.grid[row][coll] == 7:
                        self.showGold(screen,self.x + coll * self.cellSize+5, self.y + row*self.cellSize+5)"""
        #pygame.draw.line(screen,(0,0,0),(self.x + 1, self.yEnd),(self.xEnd -1, self.yEnd),2)