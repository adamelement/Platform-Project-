import pygame
pygame.init()
from character import Character
class Stage():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.stage_top = pygame.Rect(dkknds, dimensions[1], dimensions[2], dimensions[3])
        self.stage_bottomr = pygame.Rect()
        self.stage_bottoml = pygame.Rect()

    def ground_collision(self):
        if self.stage_top.colliderect(self.player1.rect):
            self.player1.y -= 1 
            self.player1.airborn = False
        else:
            self.player1.airborn = True
        if self.stage_top.colliderect(self.player2.rect):
            self.player2.y -= 1 
            self.player2.airborn = False
        else:
            self.player2.airborn = True
        if self.player1.airborn:
            self.player1.gravity()
        if self.player2.airborn:
            self.player2.gravity()

    def stage_collision(self):
        if self.stage_bottomr.colliderect(self.player1.rect):
            self.player1.x += 1
        if self.stage_bottoml.colliderect(self.player1.rect):
            self.player1.x -= 1
        if self.stage_bottomr.colliderect(self.player2.rect):
            self.player2.x += 1
        if self.stage_bottoml.colliderect(self.player2.rect):
            self.player2.x -= 1
    

    

