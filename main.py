"""
Entry point for the platform fighter game.
Creates a Game object and starts the game loop.
"""
"""import pygame

from game import Game

if __name__ == "__main__":
    game = Game()
    game.run()
"""

import pygame
import math
import sys
from stage import Stage

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
BACKGROUND_COLOUR = (0, 0, 0)
CAPTION = 'Platform Fight!'
FPS = 60
PLAYER1_COLOUR = (0, 0, 255)
PLAYER2_COLOUR = (255, 255, 0)
HITBOX_COLOUR = (255, 0, 255)


class Hitbox:
    def __init__(self, dimensions, knockback, launch_angle):
        self.hitbox = pygame.Rect(dimensions)
        self.knockback = knockback
        self.launch_angle = launch_angle


attack = ''
class InputHandler():

    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2

    def read_keyboard(self):

        keys = pygame.key.get_pressed()
        pressed_count = sum(keys)
        # if keys[pygame.K_a] or keys[pygame.K_LEFT] and pressed_count == 1:
        #     self.character1.moving_left()
        # if keys[pygame.K_d] or keys[pygame.K_RIGHT]  and pressed_count == 1:
        #     self.character1.moving_right()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.character1.movement_left()
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.character1.movement_right()
        else:
            self.character1.stop()


        if keys[pygame.K_q]:
            if not self.character1.airborn:
                self.character1.jump()
                self.character1.airborn = True
                self.character1.double_jump = False
            elif self.character1.airborn and not self.character1.double_jump:
                self.character1.jump()
                self.character1.double_jump = True

        if keys[pygame.K_z]:
            global attack
            if not self.character1.airborn:
                if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_d] or keys[pygame.K_a]:
                    attack = 'f_tilt'
                elif keys[pygame.K_w] or keys[pygame.K_UP]:
                    attack = 'up_tilt'
                elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    attack = 'down_tilt'
                else:
                    attack = 'jab'

            if self.character1.airborn:
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    if self.character1.facing_right:
                        attack = 'fair'
                    if not self.character1.facing_right:
                        attack = 'bair'
                elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    if not self.character1.facing_right:
                        attack = 'fair'
                    if self.character1.facing_right:
                        attack = 'bair'
                elif keys[pygame.K_w] or keys[pygame.K_UP]:
                    attack = 'up_air'
                elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    attack = 'down_air'
                else:
                    attack = 'nair'

        if keys[pygame.K_x]:
            if keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                attack = 'f_smash'
            elif keys[pygame.K_w] or keys[pygame.K_UP]:
                attack = 'up_smash'
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                attack = 'down_smash'

        if keys[pygame.K_c]:
            if keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[pygame.K_a] or keys[pygame.K_LEFT]:
                attack = 'side_b'
            elif keys[pygame.K_w] or keys[pygame.K_UP]:
                attack = 'up_b'
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                attack = 'down_b'
            else:
                attack = 'neutral_b'

        if keys[pygame.K_LSHIFT]:
            if self.character1.airborn:
                # self.character1.airdodge()
                pass

            if not self.character1.airborn:
                # self.character1.shield()
                pass

                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    if self.character1.facing_right:
                        # self.character1.f_roll()
                        pass
                    if not self.character1.facing_right:
                        # self.character1.r_roll()
                        pass
                elif keys[pygame.K_a or keys[pygame.K_LEFT]]:
                    if self.character1.facing_right:
                        # self.character1.b_roll()
                        pass
                    if not self.character1.facing_right:
                        # self.character1.f_roll()
                        pass
                elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    # self.character1.spotdodge()
                    pass
                elif keys[pygame.K_z]:
                    attack = 'grab'

        if keys[pygame.K_LCTRL]:
            if not self.character1.airborn:
                attack = 'grab'
        if len(attack) != 0:
            self.character1.attack(attack)
            self.character1.animation(attack)
            attack = ''
        else:
            if self.character1.airborn:
                attack = 'airidle'
            elif not self.character1.airborn:
                attack = 'idle'
            self.character1.animation(attack)
            attack = ''

        # if keys[pygame.K_j] and keys == 1:
                # if keys[pygame.K_j] and keys == 1:
        #     self.character2.moving_left()
        # if keys[pygame.K_l] and keys == 1:
        #     self.character2.moving_right()

        if keys[pygame.K_j]:
            self.character2.movement_left()
        elif keys[pygame.K_l]:
            self.character2.movement_right()
        else:
            self.character2.stop()



        if keys[pygame.K_u]:
            if not self.character2.airborn:
                self.character2.jump()
                self.character2.airborn = True
                self.character2.double_jump = False
            elif self.character2.airborn and not self.character2.double_jump:
                self.character2.jump()
                self.character2.double_jump = True

        if keys[pygame.K_m]:
            if not self.character2.airborn:
                if keys[pygame.K_l] or keys[pygame.K_j]:
                    attack = 'f_tilt'
                    self.character2.attack(attack)
                elif keys[pygame.K_i]:
                    attack = 'up_tilt'
                    self.character2.attack(attack)
                elif keys[pygame.K_k]:
                    attack = 'down_tilt'
                    self.character2.attack(attack)
                else:
                    attack = 'jab'
                    self.character2.attack(attack)

            if self.character2.airborn:
                if keys[pygame.K_l]:
                    if self.character2.facing_right:
                        attack = 'fair'
                        self.character2.attack(attack)
                    if not self.character2.facing_right:
                        attack = 'bair'
                        self.character2.attack(attack)
                elif keys[pygame.K_j]:
                    if not self.character2.facing_right:
                        attack = 'fair'
                        self.character2.attack(attack)
                    if self.character2.facing_right:
                        attack = 'bair'
                        self.character2.attack(attack)
                elif keys[pygame.K_i]:
                    attack = 'up_air'
                    self.character2.attack(attack)
                elif keys[pygame.K_k]:
                    attack = 'down_air'
                    self.character2.attack(attack)
                else:
                    attack = 'nair'
                    self.character2.attack(attack)

        if keys[pygame.K_COMMA]:
            if keys[pygame.K_l] or keys[pygame.K_j]:
                attack = 'f_smash'
                self.character2.attack(attack)
            elif keys[pygame.K_i]:
                attack = 'up_smash'
                self.character2.attack(attack)
            elif keys[pygame.K_k]:
                attack = 'down_smash'
                self.character2.attack(attack)

        if keys[pygame.K_PERIOD]:
            if keys[pygame.K_l] or keys[pygame.K_j]:
                attack = 'side_b'
                self.character2.attack(attack)
            elif keys[pygame.K_i]:
                attack = 'up_b'
                self.character2.attack(attack)
            elif keys[pygame.K_k]:
                attack = 'down_b'
                self.character2.attack(attack)
            else:
                attack = 'neutral_b'
                self.character2.attack(attack)

        if keys[pygame.K_n]:
            if self.character2.airborn:
                # self.character2.airdodge()
                pass

            if not self.character2.airborn:
                # self.character2.shield()
                pass

                if keys[pygame.K_l]:
                    if self.character2.facing_right:
                        # self.character2.f_roll()
                        pass
                    if not self.character2.facing_right:
                        # self.character2.r_roll()
                        pass
                elif keys[pygame.K_j]:
                    if self.character2.facing_right:
                        # self.character2.b_roll()
                        pass
                    if not self.character2.facing_right:
                        # self.character2.f_roll()
                        pass
                elif keys[pygame.K_k]:
                    # self.character2.spotdodge()
                    pass
                elif keys[pygame.K_m]:
                    attack = 'grab'
                    self.character2.attack(attack)
        if keys[pygame.K_SPACE]:
            if not self.character2.airborn:
                attack = 'grab'
        if len(attack) != 0:
            self.character2.attack(attack)
            self.character2.animation(attack)
            attack = ''
        else:
            if self.character2.airborn:
                attack = 'airidle'
            elif not self.character2.airborn:
                attack = 'idle'
            self.character2.animation(attack)
            attack = ''

    def controller_read(self):
        return


class Character:
    MOVEMENT_ACCEL = 0.06
    FRICTION       = 0.78

    def __init__(self, x, y, jump_height, movement_speed, weight, lives, max_speed, moveset, percent, facing_right, airborn):
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

        self.double_jump = False

        self.current_image = None
        self.frame_index = 0

        self.images = []
        self.hitboxes = []
        self.rect = pygame.Rect(self.x, self.y, 40, 60)
        self.colour = (255, 255, 255)

        self.vx = 0.0
        self.vy = 0.0

        #self.moving_left = False
        #self.moving_right = False

    def moving_right(self):
        self.movement_right()

    def moving_left(self):
        self.movement_left()

    def movement_right(self):
        if self.airborn == False:
            self.facing_right = True
        if self.vx < self.max_speed:
            #self.moving_right = True
            #self.moving_left = False
            horiz_acceleration = self.max_speed / 10
            self.vx += horiz_acceleration
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.vx = 0.0

    def movement_left(self):
        if self.airborn == False:
            self.facing_right = False
        if self.vx > -self.max_speed:
            #self.moving_left = True
            #self.moving_right = False
            horiz_acceleration = self.max_speed / 10
            self.vx -= horiz_acceleration
        if self.rect.left < 0:
            self.rect.left = 0
            self.vx = 0.0

    def stop(self):
        self.vx = 0
        #self.moving_left = False
        #self.moving_right = False
        # is_moving = self.moving_left or self.moving_right
        # if not is_moving:
        #     self.vx *= self.FRICTION

    def jump(self):
        # vert_acceleration = self.jump_height * 20
        self.vy = -15

    def short_hop(self):
        vert_acceleration = self.jump_height * 8

    def double_jump(self):
        vert_acceleration = self.jump_height * 20

    def gravity(self):
        # if vert_acceleration < self.jump_height * 20:
        #     vert_acceleration -= 1
        #     self.vy + vert_acceleration
        self.vy += 1
        if self.rect.bottom >= SCREEN_HEIGHT - 60:
            self.rect.bottom = SCREEN_HEIGHT - 60
            self.vy = 0
            self.airborn = False

    def land(self):
        vert_acceleration = 0
        airborn = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)

    def update_location(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def take_hit(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def attack(self, attack_type):
        try:
            move = self.moveset[attack_type]
        except:
            return
        try:
            hitbox_data = move['hitbox']
        except:
            return
        if hitbox_data == '' or hitbox_data is None:
            return
        self.hitboxes = []
        launch_angle = move.get('launch_angle', 0)
        knockback = move.get('knock_back', 0)
        for dimensions in hitbox_data:
            try:
                ox, oy, w, h = dimensions
                dims = [self.rect.x + ox, self.rect.y + oy, w, h]
                #dims = [self.rect.centerx + ox - w//2, self.rect.centery + oy - h//2, w, h]

                self.hitboxes.append(Hitbox(dims, knockback, launch_angle))
            except:
                pass

    def animation(self, animation_type):
        try:
            self.images = self.moveset[animation_type]['animations']
        except:
            return
        if not self.images:
            return
        self.frame_index = (self.frame_index + 1) % len(self.images)
        try:
            self.current_image = self.images[self.frame_index]
        except:
            self.current_image = None


pygame.display.init()
pygame.display.set_mode((1920, 1080))

marshal_up_tilt = []
for i in range (1,22):
    image = pygame.image.load(f'assets/sprites/Marshall_Animations/Marshall_up_tilt/Marshall_up_tilt{i}.png').convert_alpha()
    marshal_up_tilt.append(image)

marshal_d_tilt = []
for i in range (1,12):
    image = pygame.image.load(f'assets/sprites/Marshall_Animations/Marshall_d_tilt/Marshall_d_tilt{i}.png').convert_alpha()
    marshal_d_tilt.append(image)

marshal_f_tilt = []
for i in range (1,20):
    image = pygame.image.load(f'assets/sprites/Marshall_Animations/Marshall_f_tilt/Marshall_f_tilt{i}.png').convert_alpha()
    marshal_f_tilt.append(image)

marshal_dash = []
for i in range (1,11):
    image = pygame.image.load(f'assets/sprites/Marshall_Animations/Marshall_dash/Marshall_dash{i}.png').convert_alpha()
    marshal_dash.append(image)

marshal_airidle = []
for i in range(1,32):
    image = pygame.image.load(f'assets/sprites/Marshall_Animations/Marshall_AirIdle/Marshall_Airidle{i}.png').convert_alpha()
    marshal_airidle.append(image)

marshal_idle = []
for i in range(1,20):
    image = pygame.image.load(f'assets/sprites/Marshall_Animations/Marshall_Idle/Marshall_Idle{i}.png').convert_alpha()
    marshal_idle.append(image)

marshals_moves = {
    'f_tilt': {'damage' : 12 , 'knock_back' : 200, 'launch_angle': 60, 'knockback_scaling' : 1.25, 'invincibility' : 0,'hitbox' :  [(40,10,60,30)], 'startup': 7 , 'endlag': 15, 'animations' : marshal_f_tilt },
    'up_tilt': {'damage' : 8.5 , 'knock_back' : 75, 'launch_angle': 10, 'knockback_scaling' : 0.6, 'invincibility' : 0,'hitbox' :  [(10,-20,40,50)], 'startup':6 , 'endlag':15, 'animations' : marshal_up_tilt},
    'down_tilt' : {'damage' : 5 , 'knock_back' : 10, 'launch_angle': 80, 'knockback_scaling' : 0.2, 'invincibility' : 0,'hitbox' :  [(30,40,60,25)], 'startup':4 , 'endlag':12 , 'animations' : marshal_d_tilt},
    'jab' : {'damage' : 3 , 'knock_back' : 40, 'launch_angle': 20, 'knockback_scaling' : 1, 'invincibility' : 0,'hitbox' :  [(35,15,40,20)], 'startup':1 , 'endlag':5, 'animations' : marshal_idle},
    'nair' : {'damage' : 6 , 'knock_back' : 80, 'launch_angle': 45, 'knockback_scaling' : 1, 'invincibility' : 0,'hitbox' :  [(0,0,60,60)], 'startup':5 , 'endlag':10, 'animations' : marshal_airidle},
    'idle' : {'animations' : marshal_idle},
    'airidle' : {'animations' : marshal_airidle},
    'air_idle' : {'animations' : marshal_airidle}
}


class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(CAPTION)

        self.clock = pygame.time.Clock()
        self.is_running = True

        self.player1 = Character(jump_height = 31, movement_speed = 1.8, weight = 95, lives = 3, max_speed = 6, moveset = marshals_moves, facing_right = True, airborn = False, percent = 0, x = 1000, y = 500)
        self.player2 = Character(jump_height = 31, movement_speed = 1.8, weight = 95, lives = 3, max_speed = 6, moveset = marshals_moves, facing_right = False, airborn = False, percent = 0, x = 500, y = 500)
        self.players = InputHandler(self.player1, self.player2)
        self.input = InputHandler(self.player1, self.player2)
        self.stage = Stage(self.player1, self.player2)

        self.player1_attack_hitbox = None
        self.player2_attack_hitbox = None

        try:
            self.player1.current_image = self.player1.moveset['idle']['animations'][0]
        except:
            pass
        try:
            self.player2.current_image = self.player2.moveset['idle']['animations'][0]
        except:
            pass

    def run(self):
        while self.is_running:
            dt = self.clock.tick(FPS) / 1000.0

            self.handle_events()
            self.players.read_keyboard()
            self.players.controller_read()
            self.update()
            self.collide_check()
            self.draw()
            self.stage.ground_collision()

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        # pass
        self.player1.gravity()
        self.player2.gravity()
        self.player1.update_location()
        self.player2.update_location()

    def draw(self):
        self.window.fill(BACKGROUND_COLOUR)

        pygame.draw.rect(self.window, PLAYER1_COLOUR, self.player1.rect)
        pygame.draw.rect(self.window, PLAYER2_COLOUR, self.player2.rect)
        


        if self.player1.current_image is not None:
            # self.window.blit(self.player1.current_image, (self.player1.rect.x, self.player1.rect.bottom - self.player1.current_image.get_height()))
            self.window.blit(self.player1.current_image, (self.player1.rect.centerx - self.player1.current_image.get_width()//2, self.player1.rect.bottom - self.player1.current_image.get_height()))
        if self.player2.current_image is not None:
            # self.window.blit(self.player2.current_image, (self.player2.rect.x, self.player2.rect.bottom - self.player2.current_image.get_height()))
            self.window.blit(self.player2.current_image, (self.player2.rect.centerx - self.player2.current_image.get_width()//2, self.player2.rect.bottom - self.player2.current_image.get_height()))



        pygame.display.flip()

    def collide_check(self):
        try:
            player1_attack = self.player1.hitboxes
            player2_attack = self.player2.hitboxes

            for hb in player1_attack:
                if hb.hitbox.colliderect(self.player2.rect):
                    kb = hb.knockback + self.player2.percent
                    dx = kb * math.cos(hb.launch_angle * math.pi / 180) * 0.05
                    dy = -kb * math.sin(hb.launch_angle * math.pi / 180) * 0.05
                    self.player2.take_hit(dx, dy)
                    break

            for hb in player2_attack:
                if hb.hitbox.colliderect(self.player1.rect):
                    kb = hb.knockback + self.player1.percent
                    dx = kb * math.cos(hb.launch_angle * math.pi / 180) * 0.05
                    dy = -kb * math.sin(hb.launch_angle * math.pi / 180) * 0.05
                    self.player1.take_hit(dx, dy)
                    break

            self.player1.hitboxes.clear()
            self.player2.hitboxes.clear()
        except:
            pass


if __name__ == "__main__":
    game = Game()
    game.run()

"""  
if not self.player1.facing_right:
                img = pygame.transform.flip(img, True, False)
                """
