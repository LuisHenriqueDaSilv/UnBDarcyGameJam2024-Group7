from .Island import Island
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

def createWorld(spriteGroup):

  island = Island('left', 100, SCREEN_HEIGHT)
  numberOfIslands = SCREEN_WIDTH/island.rect.width
  for i in range (int(numberOfIslands)+1):
    island = Island('mid', i*island.rect.width, SCREEN_HEIGHT)
    spriteGroup.add(island)

  island = Island('mid', 100, SCREEN_HEIGHT-100)
  spriteGroup.add(island)

