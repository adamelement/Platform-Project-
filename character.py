import time
import pygame
from hitbox import Hitbox
from constants import SCREEN_WIDTH
class Character: # should just have class Character - all that should go in init
    MOVEMENT_ACCEL = 0.06 # constant, so defined here
    FRICTION       = 0.78 # adjust accordingly - the lower the value the faster the character stops - not the coefficient of friction! We should probably modify the name  
    
    def __init__(self, x, y, jump_height, movement_speed, weight, lives, max_speed, moveset, percent, facing_right, airborn): # fix airdodge
        self.x = x
        self.y = y
        self.jump_height = jump_height
        self.movement_speed = movement_speed
        self.weight = weight
        self.lives = lives
        self.max_speed = max_speed
        self.percent = percent
        self.moveset = moveset
        self.facing_right = facing_right
        self.airborn = airborn

        self.current_image = None 
        self.frame_index = 0
        
        self.images = [] 
        self.hitboxes = []
        self.rect = pygame.Rect(self.x, self.y, 40, 60) # to make contact detection easy 
        self.colour = (255, 255, 255) # colour for drawing; not needed once we use sprites

        self.vx = 0.0 # horizontal velocity 
        self.vy = 0.0

        # Input flags (these are what move_left/move_right will set)
        self.moving_left = False
        self.moving_right = False

    def movement_right(self):
        if self.airborn == False:
            facing_right = True
        if self.vx < self.max_speed:
            self.moving_right = True
            self.moving_left = False
            horiz_acceleration = self.max_speed / 10
            self.vx += horiz_acceleration
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.vx = 0.0

    def movement_left(self):
        if self.airborn == False:
            facing_right = False
        if self.vx > self.max_speed:
            self.moving_left = True
            self.moving_right = False
            horiz_acceleration = self.max_speed / 10
            self.vx -= horiz_acceleration
        if self.rect.left < 0:
            self.rect.left = 0
            self.vx = 0.0
    
    def stop(self):
        self.vx = 0
        self.moving_left = False
        self.moving_right = False
        is_moving = self.moving_left or self.moving_right
        if not is_moving:
            self.vx *= self.FRICTION # quickly approaches 0

    def jump(self):
        vert_acceleration = self.jump_height * 20

    def short_hop(self):
        vert_acceleration = self.jump_height * 8

    def double_jump(self):
        vert_acceleration = self.jump_height * 20

    def gravity(self):
        if vert_acceleration < self.jump_height * 20:
            vert_acceleration -= 1
            self.vy + vert_acceleration
        

    def land(self):
        vert_acceleration = 0
        airborn = False
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)
    
    def update_location(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def take_hit(self, x, y): #take knockback
        self.rect.x += x
        self.rect.y += y

    def attack(self, attack_type): # or just call this attack and use a flag variable to signal the kind of attack and retrieve the appropriate data from moveset
        self.hitboxes = []
        launch_angle, knockback = self.moveset[attack_type]['launch_angle'], self.moveset[attack_type]['knock_back'] # instead of ftilt, use the flag variable
        for dimensions in self.moveset[attack_type]['hitbox']:
            dimensions += [self.x, self.y, 0, 0]  
            self.hitboxes.append(Hitbox(dimensions, knockback, launch_angle))


    def animation(self, animation_type):
        #self.images =  use animation_type to retrieve the list of images from the moveset dictionary
        self.images = [self.moveset[animation_type]['animations']]
        self.current_image = self.images[self.frame_index]
        self.frame_index = (self.frame_index + 1) % len(self.images)
        if self.frame_index > 8:
            if self.frame_index == len(self.images) - 1: 
                # or whichever number to represent the attack
                self.frame_index = 0
                self.images = '' # set to default movement  
        
    




    
