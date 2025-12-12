import time

class Character: # should just have class Character - all that should go in init
    MOVEMENT_ACCEL = 0.06 # constant, so defined here
    FRICTION       = 0.78 # adjust accordingly - the lower the value the faster the character stops - not the coefficient of friction! We should probably modify the name  
    
    def __init__(self, jump_height, movement_speed, weight, lives, direction, max_speed, airdodge, moveset):
        self.jump_height = jump_height
        self.movement_speed = movement_speed
        self.weight = weight
        self.lives = lives
        self.direction = direction
        self.max_speed = max_speed
        self.percent = percent
        self.moveset = moveset

        self.current_frame = 0
        self.images = []
        self.hitboxes = []
        self.rect = pygame.Rect(x, y, 40, 60) # to make contact detection easy 
        self.colour = (255, 255, 255) # colour for drawing; not needed once we use sprites

        self.vx = 0.0 # horizontal velocity 
        self.vy = 0.0

        # Input flags (these are what move_left/move_right will set)
        self.moving_left = False
        self.moving_right = False

    def movement_right(self):
        if airborne == False:
            character_dirrection == right
        if self.vx < self.max_speed:
            self.moving_right = True
            self.moving_left = False
            horiz_acceleration = self.max_speed / 10
            self.vx += horiz_acceleration
        if self.rect.right > screen_width:
            self.rect.right = screen_width
            self.vx = 0.0

    def movement_left(self):
        if airborne == False:
            character_dirrection == left
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

    def f_tilt(self): # or just call this attack and use a flag variable to signal the kind of attack and retrieve the appropriate data from moveset
        self.hitboxes = []
        launch_angle, knockback = moveset['ftilt']['launch_angle'], moveset['ftilt']['knock_back'] # instead of ftilt, use the flag variable
        for dimensions in moveset['f_tilt']['hitbox']:
            self.hitboxes.append[Hitbox(dimensions, knockback, launch_angle)]
        
    




    
