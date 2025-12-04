import time

class Character(self, x, y, jump_height, movement_speed, weight, lives, direction, max_speed): # should just have class Character - all that should go in init
    MOVEMENT_ACCEL = 0.06 # constant, so defined here
    FRICTION       = 0.78 # adjust accordingly - the lower the value the faster the character stops - not the coefficient of friction! We should probably modify the name  
    
    def __init__(): #  def __init__(self, jump_height, movement_speed, weight, lives, direction, max_speed):
        self.jump_height = jump_height
        self.movement_speed = movement_speed
        self.weight = weight
        self.lives = lives
        self.direction = direction
        self.max_speed = max_speed

        self.rect = pygame.Rect(x, y, 40, 60) # to make contact detection easy 
        self.colour = (255, 255, 255) # colour for drawing; not needed once we use sprites

        self.vx = 0.0 # horizontal velocity 

        # Input flags (these are what move_left/move_right will set)
        self.moving_left = False
        self.moving_right = False

    def movement_right(self):
        global self.horiz_movement_speed # don't use the global keyword in classes - it's not needed and defeats the purpose of classes and encapsulation and can make debugging very tough 
        if self.horiz_movement_speed < self.max_speed:
            horiz_acceleration = self.max_speed / 10
            self.horiz_movement_speed += horiz_acceleration

    def movement_left(self):
        global self.horiz_movement_speed
        if self.horiz_movement_speed > self.max_speed:
            horiz_acceleration = self.max_speed / 10
            self.horiz_movement_speed -= horiz_acceleration
    
    def stop(self):
        global self.horiz_movement_speed
        self.horiz_movement_speed = 0

    def jump(self):
        global vert_acceleration
        vert_acceleration = self.jump_height * 20

    def short_hop(self):
        global vert_acceleration
        vert_acceleration = self.jump_height * 8

    def double_jump(self):
        global vert_acceleration
        vert_acceleration = self.jump_height * 20

    def gravity(self):
        global vert_acceleration
        vert_acceleration -= 1
        self.vert_movement_speed + vert_acceleration



        




    """ Consider these methods and physics logic 

    
    def move_left(self):
        self.moving_left = True
        self.moving_right = False

    def move_right(self):
        self.moving_right = True
        self.moving_left = False

    def stop_horizontal(self):
        self.moving_left = False
        self.moving_right = False

    
    # Physics update
    
    def update_horizontal(self, screen_width):
        """Apply Physics"""

        # Apply acceleration from input flags to velocity 
        if self.moving_left:
            self.vx -= self.MOVEMENT_ACCEL
        if self.moving_right:
            self.vx += self.MOVEMENT_ACCEL

        # Friction when not trying to move
        is_moving = self.moving_left or self.moving_right
        if not is_moving:
            self.vx *= self.FRICTION # quickly approaches 0
            

        # max speed
        self.vx = max(-self.max_speed, min(self.max_speed, self.vx))

        # Apply velocity to position
        self.rect.x += self.vx

        # Boundary collisions
        if self.rect.left < 0:
            self.rect.left = 0
            self.vx = 0.0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
            self.vx = 0.0

    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)

"""

marshal = Character( 31 , 1.8 , 95, 3, 4, 6  ) # we will probably create character objects in the game class, so this is not needed here  
    

# this should go in the moveset.py file so as to not clutter this character class, which is already going to be big enough 

marshals_moves = {'ftilt': {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'jab' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'up_tilt': {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': },
                     'down_tilt' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': },
                     'dash_attack' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'nair' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'fair' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'bair' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'dair' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'up_air' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'f_smash' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'up_smash' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'down_smash' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'neutral_b' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'up_b' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }
                     'down_b' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'side_b' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'grab' : {'damage' 0 :  , 'knock_back' 0 : '', 'launch_angle': 0 , 'knockback_scaling' 0 : , 'hitox' :  , 'startup' : , 'endlag': }, 
                     'up_throw' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'down_throw' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'back_throw' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'forward_throw' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'attack_getup' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }, 
                     'ledge_attack' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'hitox' :  , 'startup': , 'endlag': }}, 

