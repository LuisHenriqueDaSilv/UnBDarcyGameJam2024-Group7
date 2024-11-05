from .Island import Island
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

def createWorld(spriteGroup):

  midIsland = Island('mid', 100, SCREEN_HEIGHT)
  leftIsland = Island('left', 100, SCREEN_HEIGHT)
  rightIsland = Island('right', 100, SCREEN_HEIGHT)
  numberOfIslands = SCREEN_WIDTH/midIsland.rect.width
  for i in range (int(numberOfIslands)+2):
    island = Island('mid', i*midIsland.rect.width, SCREEN_HEIGHT)
    spriteGroup.add(island)

  spriteGroup.add(Island('mid', midIsland.rect.width, SCREEN_HEIGHT-130))
  spriteGroup.add(Island('mid', midIsland.rect.width*2, SCREEN_HEIGHT-130))
  spriteGroup.add(Island('right', midIsland.rect.width*3, SCREEN_HEIGHT-130))
  # island = Island('right', SCREEN_WIDTH-300, SCREEN_HEIGHT-100)

