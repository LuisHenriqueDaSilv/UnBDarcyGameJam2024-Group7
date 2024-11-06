import pygame

from src.Player import Player
from src.Background import Background
from src.createWorld import createWorld
from src.createEnemies import createEnemies
from settings import *

from settings import SCREEN_HEIGHT, SCREEN_WIDTH
pygame.init()
pygame.display.set_caption("UnB Darcy Game Jam - Grupo 07")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


allSprites = pygame.sprite.Group()
floorGroup = pygame.sprite.Group()
enemiesGroup = pygame.sprite.Group()
backgroundGroup = pygame.sprite.Group()

baseBackground = Background(0)
for i in range(3):
  backgroundGroup.add(Background(-i*baseBackground.rect.height))

player = Player()

allSprites.add(player)

createWorld(floorGroup)
createEnemies(enemiesGroup)

running = True
while running:

  clock.tick(FPS) 
  screen.fill((0, 0, 0))

  playerCollidesWithFloor = pygame.sprite.spritecollide(player, floorGroup, False)
  leftCollide = False
  rightCollide = False
  bottomCollide = False
  topCollide = False
  for collide in playerCollidesWithFloor:
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
  player.bottomCollide = bottomCollide
  player.topCollide = topCollide
  player.leftCollide = leftCollide
  player.rightCollide = rightCollide
    
  playerCollidesWithEnemies = pygame.sprite.spritecollide(player, enemiesGroup, False)
  for enemie in playerCollidesWithEnemies: 
    if player.currentStatus == 'attack':
      if player.lastMove > 0: 
        enemie.hit(15, 0)
      else:
        enemie.hit(15, 1)
    elif enemie.currentStatus == 'attack':
      player.hit(enemie.damage)
  
  key = pygame.key.get_pressed()
  if key[pygame.K_a] and player.bottomCollide and not player.currentStatus == 'attack' and not player.currentStatus == 'death':
    player.run(-5)
  elif key[pygame.K_d] and player.bottomCollide and not player.currentStatus == 'attack' and not player.currentStatus == 'death':
    player.run(5)
  elif key[pygame.K_f] and not player.currentStatus == 'attack' and not player.currentStatus == 'death':
    player.attack()
  elif player.bottomCollide and not player.currentStatus == 'attack' and not player.currentStatus == 'death':
    player.xSpeed = 0
    player.changeStatus('idle')
  
  if key[pygame.K_SPACE] and not player.currentStatus == 'death':
    player.jump()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  for background in backgroundGroup:
    background.update(player.rect.y, player.ySpeed)

  backgroundGroup.draw(screen)
  allSprites.update()
  allSprites.draw(screen)
  
  for floor in floorGroup: 
    floor.update(player.rect.y, player.ySpeed)
  floorGroup.draw(screen)

  for enemie in enemiesGroup:
    enemie.update(player.rect.y, player.ySpeed, player)
    
  enemiesGroup.draw(screen)
  pygame.display.flip()

pygame.quit()