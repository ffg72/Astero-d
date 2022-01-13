import random

from pygame.math import Vector2

import core
from asteroid import Asteroids
from vaisseau1 import Vaisseaux


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [1200, 850]

    print("Setup END-----------")

    core.memory("listeAsteroid", [])
    core.memory("vaisseau1",Vaisseaux())
    core.memory("asteroid",Asteroids())

    for a in range(20):
        core.memory("listeAsteroid").append(Asteroids())
        print(core.memory("listeAsteroid"), [a])

def run():
    core.cleanScreen()
    for a in core.memory("listeAsteroid"):
        a.affichage(core.screen)

    print(core.getKeyPressList(True))

    core.memory("vaisseau1").affichage()
    #core.memory("vaisseau1").move(core.getMouseLeftClick())
    #core.memory("asteroid").affichage(screen)
    #core.memory("asteroid").move()

    #for a in core.memory("listeAsteroid"):
        #a.collision(core.memory("vaisseau1"))

core.main(setup, run)
