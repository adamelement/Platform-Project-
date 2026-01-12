import pygame()
class HUD:
    def __init__(self, percent, lives, position, size)
        self.percent = pygame.Character(percent)
        self.lives = pygame.Character(lives)
        self.position = position
        self.size = size
    p1_hud = pygame.image.load('assets/backgrounds/hud_assets/hud.webp').convert_alpha
    p2_hud = pygame.image.load('assets/backgrounds/hud_assets/hud.webp').convert_alpha