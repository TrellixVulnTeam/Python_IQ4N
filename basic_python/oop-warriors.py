
import random
import math

class Worrior:
    def __init__(self,name="warrior",health=0,attackmax=0,blockmax=0):
        self.name = name
        self.health = health
        self.attackmax = attackmax
        self.blockmax = blockmax

    def attack(self):
        attkamt = self.attackmax * (random.random())


