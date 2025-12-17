import pygame
pygame.init()

class Hitbox:
    def __init__(self, dimensions, knockback, launch_angle):
        self.hitbox = pygame.Rect(dimensions)
        self.knockback = knockback
        self.launch_angle = launch_angle

   # def attack_hitbox(self):




