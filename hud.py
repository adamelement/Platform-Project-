import pygame
import constants
class HUD:
    def __init__(self, percent, lives, position, size)
        self.percent = pygame.Character(percent)
        self.lives = pygame.Character(lives)
        self.position = position
        self.size = size
    p1_hud = pygame.image.load('assets/backgrounds/hud_assets/hud.webp').convert_alpha()
    p2_hud = pygame.image.load('assets/backgrounds/hud_assets/hud.webp').convert_alpha()
    hud1_sprite = p1_hud.get_rect()
    hud2_sprite = p2_hud.get_rect()

    hud1_sprite.center = (constants.SCREEN_WIDTH//1.3, constants.SCREEN_HEIGHT//5)
    hud2_sprite.center = (constants.SCREEN_WIDTH//4, constants.SCREEN_HEIGHT//5)



(in mainevean)

    from filename import class_name
        
    from hud import HUD

    hud_object = HUD(value, value2,....)

    hud_object.attribute
    hud_object.method()
