import random
import pygame

from pathlib import Path


"""
0 empty att
1 empty not att
2 dirt att
3 dirt not att
4 ax att
5 ax not att
6 money att
7 money not att
"""


class MineGrid:
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
        Odd values are given to all, meaning the blocks are initially non-reachable.
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

    def __init__(self):
        self.numRows = 7
        self.numCol = 5
        self.cellSize = 30
        self.x = 50
        self.y = 50
        self.head = [(self.assignRandom()-1) for i in range(self.numCol)]
        self.grid = [[self.assignRandom() for j in range(self.numCol)] for i in range(self.numRows)]
        self.bottom = [self.assignRandom() for i in range(self.numCol)]
        self.grid[0][0] = 0
        att = [(0, 0)]
        self.findAttainable(att)
        #self.colourArr = self.getCellColours()
        self.xEnd = self.x + self.numCol * self.cellSize
        self.yEnd = self.y + self.numRows * self.cellSize

    def findAttainable(self, att):
        for tup in att:
            if tup[1] < (self.numRows-1):
                if self.grid[tup[1]+1][tup[0]] % 2 == 1:
                    self.grid[tup[1]+1][tup[0]] -= 1
                    if self.grid[tup[1]+1][tup[0]]== 0:
                        att.append([tup[0], tup[1]+1])
            elif tup[1] == (self.numRows -1):
                if self.bottom[tup[0]] % 2 == 1:
                    self.bottom[tup[0]] -= 1
                    if self.bottom[tup[0]] == 0:
                        att = self.addLevel(tup[0], att)
                        tup[1] -= 1
            else:
                att = self.addLevel(tup[0],att)
                tup[1] -= 1
            if tup[1] != 0:
                if self.grid[tup[1] -1][tup[0]] % 2 == 1:
                    self.grid[tup[1] - 1][tup[0]] -= 1
                    if self.grid[tup[1] -1][tup[0]] == 0:
                        att.append([tup[0], tup[1]-1])
            if tup[0] != 0:
                if self.grid[tup[1]][tup[0] -1] % 2 == 1:
                    self.grid[tup[1]][tup[0] - 1] -= 1
                    if self.grid[tup[1]][tup[0] -1] == 0:
                        att.append([tup[0] -1, tup[1]])
            if tup[0] != (self.numCol -1):
                if self.grid[tup[1]][tup[0] +1] % 2 == 1:
                    self.grid[tup[1]][tup[0] + 1] -= 1
                    if self.grid[tup[1]][tup[0] +1] == 0:
                        att.append([tup[0]+1, tup[1]])
        #Proxim Morin
        #Sylvie Vincent

    def addLevel(self, xhit, att):
        self.head = self.grid[0]
        for l in range(self.numRows-1):
            self.grid[l] = self.grid[l+1]
        self.grid[self.numRows-1] = self.bottom
        self.bottom = [self.assignRandom() for a in range(self.numCol)]
        self.bottom[xhit] -= 1
        if self.bottom[xhit] == 0:
            att.append([xhit, self.numRows])
        return att


    def print_grid(self):
        for row in range(self.numRows):
            for column in range(self.numCol):
                print(self.grid[row][column], end = " ")
            print()

    def draw(self, screen):
        for row in range(self.numRows):
            for coll in range(len(self.grid[row])):
                if self.grid[row][coll] != 0:
                    if self.grid[row][coll] == 1:
                        myColor = self.emptyNA
                    elif self.grid[row][coll] % 2 == 0:
                        myColor = self.general
                    else:
                        myColor = self.generalNA
                    cellRect = pygame.Rect(self.x + coll * self.cellSize+1, self.y + row*self.cellSize+1, self.cellSize-1, self.cellSize-1)
                    pygame.draw.rect(screen, myColor, cellRect)
                    if self.grid[row][coll] == 4 or self.grid[row][coll] == 5:
                        self.showPickaxe(screen,self.x + coll * self.cellSize+5, self.y + row*self.cellSize+5)
                    elif self.grid[row][coll] == 6 or self.grid[row][coll] == 7:
                        self.showGold(screen,self.x + coll * self.cellSize+5, self.y + row*self.cellSize+5)
        pygame.draw.line(screen,(0,0,0),(self.x + 1, self.yEnd),(self.xEnd -1, self.yEnd),2)
        for bl in range(self.numCol):
            cellRect = pygame.Rect(self.x + bl * self.cellSize +1, self.yEnd+3, self.cellSize-1, self.cellSize-1)
            if self.bottom[bl] == 1:
                myColor = self.emptyNA
            elif self.bottom[bl] % 2 == 0:
                myColor = self.general
            else:
                myColor = self.generalNA
            pygame.draw.rect(screen, myColor, cellRect)
            if self.bottom[bl] == 4 or self.bottom[bl] == 5:
                self.showPickaxe(screen, self.x + bl * self.cellSize + 5, self.yEnd+8)
            elif self.bottom[bl] == 6 or self.bottom[bl] == 7:
                self.showGold(screen, self.x + bl * self.cellSize + 5, self.yEnd+8)