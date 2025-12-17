import pygame


'''(((((percent / 10 + (percent * damage) / 20) * 200 / (weight +10 ) * 1.4) + 18) * knockback_scaling) + knock_back) * r



1 + (p - 35 )(115)*0.1'''

marshal_up_tilt = []
for i in range (1,22):
    image = pygame.image.load(f'Platform-Project\assets\sprites\Marshall_Animations\Marshall_dash/Marshal_up_tilt{i}.png').convert_alpha()
    marshal_up_tilt.append(image)
    marshal_up_tilt = []

marshal_d_tilt = []
for i in range (1,12):
    image = pygame.image.load(f'Platform-Project\assets\sprites\Marshall_Animations\Marshall_dash/Marshal_d_tilt{i}.png').convert_alpha()
    marshal_up_tilt.append(image)
    marshal_up_tilt = []

marshal_f_tilt = []
for i in range (1,20):
    image = pygame.image.load(f'Platform-Project\assets\sprites\Marshall_Animations\Marshall_dash/Marshal_f_tilt{i}.png').convert_alpha()
    marshal_up_tilt.append(image)

marshal_dash = []
for i in range (1,11):
    image = pygame.image.load(f'Platform-Project\assets\sprites\Marshall_Animations\Marshall_dash/Marshal_dash{i}.png').convert_alpha()
    marshal_dash.append(image)

marshal_airidle = []
for i in range(1,32):
    image = pygame.image.load(f'Platform-Project\assets\sprites\Marshall_Animations\Marshall_AirIdle/Marshal_Airidle{i}.png').convert_alpha()
    marshal_airidle.append(image)

 # we will probably create character objects in the game class, so this is not needed here  
    

# this should go in the moveset.py file so as to not clutter this character class, which is already going to be big enough 
# hitbox [[length, width, (x relative to player, y relative to player)], [second hitbox stats] ]

class character_moveset:
    def __init__(self, damage, knockback, launch_angle, knockback_scaling, invincibility, hitbox, startup, endlag):
        self.damage = damage
        self.knockback = knockback
        self.launch_angle = launch_angle
        self.knockback_scaling = knockback_scaling
        self.invincibility = invincibility
        self.hitbox = hitbox
        self.startup = startup
        self.endlag = endlag
#move name = character_moveset(damage, base knockback, launch angle in degrees, knockback scaling multiplier, invuln, hitbox location, startup, endlag)
f_tilt = character_moveset(12, 200, 60, 1.25, 0, '''blank for now''', 7, 15 )
down_tilt = character_moveset(5, 10, 80, 0.2, 0, '''blank for now''', 4, 12, )
up_tilt = character_moveset(8.5, 75, 10, 0.6, 0, '''blank for now''', 6, 15) 
nair = character_moveset(9.5, 90, 45, 1, 0, '''blank for now''', 5, 20)
fair = character_moveset(10, 200, 75, 1.1, 0, '''blank for now''', 8, 20 )
up_air = character_moveset(10, 100, -10, 1, 0, '''blank for now''', 8, 16)
bair = character_moveset(15, 75, 300, 1.4, 0, '''blank for now''', 14, 24)
dair = character_moveset(12, 100, 175, 0.75, 0, '''blank for now''', 15, 25)

#old moveset, changed the moves into a class and defines a few of their stats
marshals_moves = {'f_tilt': {'damage' : 12 , 'knock_back' : 200, 'launch_angle': 60, 'knockback_scaling' : 1.25, 'invincibility' : 0,'hitbox' :  '', 'startup': 7 , 'endlag': 15, 'animations' : marshal_f_tilt }, 
                     'jab1' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' },
                     'jab2' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' },
                     'rappid_jab' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'', 'animations' : '' }, 
                     'up_tilt': {'damage' : 8.5 , 'knock_back' : 75, 'launch_angle': 10, 'knockback_scaling' : 0.6, 'invincibility' : 0,'hitbox' :  '', 'startup':6 , 'endlag':15, 'animations' : marshal_up_tilt},
                     'down_tilt' : {'damage' : 5 , 'knock_back' : 10, 'launch_angle': 80, 'knockback_scaling' : 0.2, 'invincibility' : 0,'hitbox' :  '', 'startup':4 , 'endlag':12 , 'animations' : marshal_d_tilt},
                     'dash_attack' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'nair' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'fair' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'bair' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'dair' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'up_air' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'f_smash' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'up_smash' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'down_smash' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'neutral_b' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '','invincibility' : '', 'hitbox' : '' , 'startup': '', 'endlag': '' }, 
                     'up_b' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' },
                     'down_b' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'side_b' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'grab' : {'damage' :0  , 'knock_back' :0 , 'launch_angle': 0 , 'knockback_scaling' :0 , 'invincibility' : '','hitbox' :  '', 'startup' : '', 'endlag':'' }, 
                     'up_throw' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'down_throw' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'back_throw' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'forward_throw' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'attack_getup' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'ledge_attack' : {'damage' : '' , 'knock_back' : '', 'launch_angle': '', 'knockback_scaling' : '', 'invincibility' : '','hitbox' :  '', 'startup':'' , 'endlag':'' }, 
                     'airddoge' : {'damage' : 0, 'knock_back' :0 , 'launch_angle': 0 , 'knockback_scaling' :0 , 'invincibility' : (3, 30),'hitbox' : '' , 'startup' : 3, 'endlag': 49}}
