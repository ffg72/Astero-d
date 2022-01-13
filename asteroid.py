import random
import pygame
from pygame.math import Vector2


class Asteroids:
    def __init__(self):
        self.taille = 5
        self.couleur = (255, 255, 255)
        self.masse = 3
        self.position = Vector2(random.randint(0,1600),random.randint(0,850))
        self.vitesse = 5
        self.vitesseMin = Vector2(0, 0)
        self.vitesseMax = 2
        self.k = 0.01
        self.l0 = 1
        self.accMax = 0.5
        self.intact = True

    def affichage(self,screend):

        pygame.draw.circle(screen, self.couleur, self.position, self.taille)

    '''
def move(self):
        if self.intact = True:
            self.acceleration = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

            if self.acceleration.length() > self.accMax:
                self.acceleration.scale_to_length(self.accMax)

            self.vitesse = self.vitesse + self.acceleration

            if self.vitesse.length() > self.vitesseMax:
                self.vitesse.scale_to_length(self.vitesseMax)

            self.position = self.position + self.vitesse

            self.acceleration = Vector2(0, 0)'''



    '''
        def explosion (self, avatar):

               if vaisseau1.position.distance_to(self.position) < self.taille + vaisseau1.taille:
                   self.position = Vector2(random.randint(0, 1600), random.randint(0, 850))
                   self.vitesse = 5
                   self.couleur = (255,255,255)
        '''


    def getPosition(self):
        return self.position









