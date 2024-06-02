import pygame
import sys

from myMine.MineGrid import MineBlock, MineGrid
from myMine.Player import Player, playerInfo

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Testing")
clock = pygame.time.Clock()

mine = MineGrid()
player = Player("test", mine)
playerIcon = pygame.image.load('Pictures/icons8-miner-30.png')
playInfo = playerInfo(player, mine)

def icon(x,y):
    screen.blit(playerIcon,(x,y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.move("left")
                #player.moveLeft()
                #mine.print_grid()
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.move("right")
                #player.moveRight()
                #mine.print_grid()
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                player.move("up")
                #player.moveUp()
                #mine.print_grid()
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.move("down")
                #player.moveDown()
                #mine.print_grid()
    screen.fill((122,129,255))
    mine.draw(screen)
    player.draw(screen)
    playInfo.draw(screen)
    #icon(50,50)
    pygame.display.update()
    clock.tick(60)