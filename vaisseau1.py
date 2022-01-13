import pygame
from pygame.math import Vector2
from pygame.transform import rotate

import core


class Vaisseaux:
    def __init__(self):
        self.taille = 10
        self.couleur = (255, 255, 255)
        self.position = Vector2(400, 400)
        self.vitesse = Vector2(0, 0)
        self.vitesseMin = Vector2(0, 0)
        self.vitesseMax = 2
        self.k = 0.01
        self.l0 = 1
        self.accMax = 0.5
        self.vecteur = Vector2(0,200)
    #Ax, Ay = 50, 100
    #Bx, By = 100, 50
    #Cx, Cy = 160, 350


    def affichage(self, Ax=50, Ay=100, Bx=100, By=50, Cx=100, Cy=100):
        #core.Draw.polygon(self.couleur, , 2)
        pygame.draw.line(core.screen, self.couleur, (Ax, Ay), (Bx, By), 2)
        pygame.draw.line(core.screen,self.couleur, (Cx, Cy), (Bx, By), 2)
        pygame.draw.line(core.screen,self.couleur, (Ax, Ay), (Cx, Cy), 2)

    def move(self):
        self.vecteur.magnitude()

        '''Z'''
        if core.getKeyPressList('z'):
            self.vecteur.scale_to_length(self.vecteur).magnitude() + 10

        '''Q'''
        if core.getKeyPressList(113):
            self.vecteur.rotate(-1)

        '''D'''
        if core.getKeyPressList(100):
            self.vecteur.rotate(1)

            # bilan des forces
            # F=k * u * |l-l0|

        l = self.position.distance_to(self.vecteur)
        u = self.vecteur - self.position
        u = u.normalize()

        F = self.k * u * abs(l - self.l0) / self.taille


            # limiter la force max
        if F.length() > self.accMax:
            F.scale_to_length(self.accMax)

            # ajouter la force a la vitesse
        self.vitesse = self.vitesse + F

            # limiter la vitesse

        if self.vitesse.length() > self.vitesseMax-self.taille*0.05:
            self.vitesse.scale_to_length(self.vitesseMax-self.taille*0.05)

        # ajouter la vitesse a la position

        self.position = self.position + self.vitesse



    def tirer (self):
            pass



    def setVitesse(self, v):
        self.vitesse = v

    def setPosition(self, pos):
        self.position = pos

    def getVitesse(self):
        return self.vitesse

    def getPosition(self):
        return self.position

    def getTaille(self):
        return self.taille