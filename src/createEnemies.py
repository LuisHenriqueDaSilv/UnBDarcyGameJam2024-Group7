from .DemonFly import DemonFly
from .DemonAxe import DemonAxe
from .Wizard import Wizard
from settings import SCREEN_HEIGHT

def createEnemies(spriteGroup):
  demonAxeBase = DemonAxe(0, 0, 0)
  wizardBase = Wizard(0, 0, 0)
  spriteGroup.add(DemonFly(550, 0, 100))
  spriteGroup.add(Wizard(SCREEN_HEIGHT-128/2.5-demonAxeBase.rect.height, 0, 600))
