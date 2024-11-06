from .DemonFly import DemonFly
from .DemonAxe import DemonAxe
from settings import SCREEN_HEIGHT

def createEnemies(spriteGroup):
  spriteGroup.add(DemonFly(550, 0, 100))
  demonAxeBase = DemonAxe(0, 0, 0)
  spriteGroup.add(DemonAxe(SCREEN_HEIGHT-128/2.5-demonAxeBase.rect.height, 0, 600))
