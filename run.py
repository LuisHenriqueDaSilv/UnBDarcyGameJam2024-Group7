import pygame

from src.Player import Player
from src.Island import Island
from src.createWorld import createWorld
from settings import *

pygame.init()
pygame.display.set_caption("UnB Darcy Game Jam - Grupo 07")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


allSprites = pygame.sprite.Group()
floorGroup = pygame.sprite.Group()

player = Player()
allSprites.add(player)

createWorld(floorGroup)

running = True
while running:

  clock.tick(FPS) 
  screen.fill((0, 0, 0))

  playerCollides = pygame.sprite.spritecollide(player, floorGroup, False)
  leftCollide = False
  rightCollide = False
  bottomCollide = False
  topCollide = False
  for collide in playerCollides:
     
    playerFoot = player.rect.height+player.rect.y
    playerHead = player.rect.y
    blockBottom = collide.rect.y + collide.rect.height 
    playerRight = player.rect.x+player.rect.height
    blockLeft = collide.rect.x + collide.rect.width
    if collide.rect.y-15 < playerFoot and collide.rect.y+15 > playerFoot:
      bottomCollide = True
    elif playerHead+15 > blockBottom and playerHead -15 < blockBottom:
      topCollide = True
    elif playerRight+15 > collide.rect.x and playerRight-15 < collide.rect.x: 
      rightCollide = True
    elif blockLeft +15 > player.rect.x and blockLeft-15 < player.rect.x:
      leftCollide = True
    # print("============")
    # print(collide.rect.x)
    # print(playerRight)
    
  player.bottomCollide = bottomCollide
  player.topCollide = topCollide
  player.leftCollide = leftCollide
  player.rightCollide = rightCollide


  key = pygame.key.get_pressed()
  if key[pygame.K_a] and player.bottomCollide:
    player.run(-5)
  elif key[pygame.K_d] and player.bottomCollide:
    player.run(5)
  elif player.bottomCollide:
    player.xSpeed = 0
    player.changeStatus('idle')

  if key[pygame.K_SPACE]:
    player.jump()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    
  allSprites.draw(screen)
  allSprites.update()
  floorGroup.draw(screen)
  floorGroup.update()
  pygame.display.flip()

pygame.quit()