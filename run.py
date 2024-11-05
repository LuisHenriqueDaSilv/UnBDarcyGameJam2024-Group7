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

  if not pygame.sprite.spritecollide(player, floorGroup, False):
    player.ySpeed += 0.2
    player.falling = True;
  else: 
    player.ySpeed = 0;
    player.falling = False;

  key = pygame.key.get_pressed()
  if key[pygame.K_a]:
    player.run(-5)
  elif key[pygame.K_d]:
    player.run(5)
  else:
    player.changeStatus('idle')

  if key[pygame.K_SPACE]  and not player.falling:
    print("pulou")
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