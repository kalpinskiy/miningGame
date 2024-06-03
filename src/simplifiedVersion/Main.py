import pygame
import sys

from src.simplifiedVersion.MineGrid import MineGrid
from src.simplifiedVersion.Player import Player, playerInfo

pygame.init()


screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Testing")
clock = pygame.time.Clock()

mine = MineGrid()
player = Player("test", mine)
playInfo = playerInfo(player, mine)
playInfo = playerInfo(player, mine)

def icon(x,y):
    screen.blit(Player.playerIcon,(x,y))

#mine.grid[1][3] = 3
#mine.grid[2][4] = 1

#mine.print_grid()

while True:
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
        pygame.quit()
        sys.exit()
    screen.fill((122,129,255))
    mine.draw(screen)
    player.draw(screen)
    playInfo.draw(screen)
    #icon(50,50)
    pygame.display.update()
    clock.tick(60)