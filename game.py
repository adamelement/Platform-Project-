



import sys
import pygame
import math
from movesets import marshals_moves

from constants import (
SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOUR,
    CAPTION,
    FPS,
    PLAYER1_COLOUR, # will not be shown once sprites are blitted on,
    PLAYER2_COLOUR, # will not be shown once sprites are present, 
    HITBOX_COLOUR # will not be drawn, making these hitboxes effectively invisible,
)               


from character import Character
from input_handler import InputHandler
from hitbox import Hitbox


class Game:
    """
    Manages the entire game loop and high-level game logic.

    Responsibilities:
    - Initialize pygame, window, and stage
    - Create and update characters
    - Handle input via input_handler
    - Handle attack hitboxes and knockback
    - Draw everything each frame
    """
    # moveset = {'f_tilt': {'hitboxes': [(100,100,50,50), (200, 200, 100, 100)], 'launch_angle': 45, 'knock_back': 20}}
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(CAPTION)

        self.clock = pygame.time.Clock()
        self.is_running = True

        # Stage
        #self.stage = Stage()

        # Two fighting characters 
        self.player1 = Character(jump_height = 31, movement_speed = 1.8, weight = 95, lives = 3, max_speed = 6, moveset = marshals_moves, facing_right = True, airborn = False, percent = 0, x = 1000, y = 1000)
        self.player2 = Character(jump_height = 31, movement_speed = 1.8, weight = 95, lives = 3, max_speed = 6, moveset = marshals_moves, facing_right = False, airborn = False, percent = 0, x = 500, y = 500)
        self.players = InputHandler(self.player1, self.player2)
        # Input handling objects for both characters 
        self.input = InputHandler(self.player1, self.player2)

        # Attack hitboxes (spawned when attacking) 
      
        self.player1_attack_hitbox = None
        self.player2_attack_hitbox = None

    def run(self):
        """Main game loop."""
        while self.is_running:
            dt = self.clock.tick(FPS) / 1000.0  # dt ready for later use

            self.handle_events()
            self.players.read_keyboard()
            self.players.controller_read()
            self.update()
            self.collide_check()
            self.draw()
            pygame.display.flip()

        pygame.quit()
        sys.exit()

  

    def handle_events(self):
        """Handle window events (close button, etc.)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

   

    def update(self):
        """Update game state: input, movement, collisions, attacks."""
        pass 

    def draw(self):
        """Draw background, characters, and hitboxes."""
        self.window.fill(BACKGROUND_COLOUR)

        # Characters boxes
        pygame.draw.rect(self.window, PLAYER1_COLOUR, self.player1.rect)
        pygame.draw.rect(self.window, PLAYER2_COLOUR, self.player2.rect)

        self.window.blit(self.player1.current_image, self.player1.x, self.player1.y) # double check to make sure attributes are defined that way and repeat for p2

        pygame.display.flip()

        # fill the screen with black ink 
    
    def collide_check(self):
        try:
            player1_attack = self.player1.hitboxes
            player1_launch_angle = self.player2.hitboxes[0][2]
            player1_knockback = self.player2.hitboxes[0][1] + self.player1.percentage # or formula for knockback 
            player1_x_displacement = player1_knockback * math.cos(player1_launch_angle * math.pi / 180)
            player1_y_displacement = player1_knockback * math.sin(player1_launch_angle * math.pi / 180)
            
            player2_attack = self.player2.hitboxes
            player2_launch_angle = self.player1.hitboxes[0][2]
            player2_knockback = self.player1.hitboxes[0][1] + self.player2.percentage
            player2_x_displacement = player2_knockback * math.cos(player1_launch_angle * math.pi / 180)
            player2_y_displacement = player2_knockback * math.sin(player1_launch_angle * math.pi / 180)

        
            for boxes in player1_attack:
                if boxes.colliderect(self.player2.rect):
                    self.player2.take_hit(player2_x_displacement, player2_y_displacement)
                    break

            for boxes in player2_attack:
                if boxes.colliderect(self.player1.rect):
                    self.player1.take_hit(player1_x_displacement, player1_y_displacement)
                    break
            
            self.player1.hitboxes.clear()
            self.player2.hitboxes.clear()
        except:
            pass



