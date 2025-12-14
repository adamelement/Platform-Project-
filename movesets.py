import pygame


(((((percent / 10 + (percent * damage) / 20) * 200 / (weight +10 ) * 1.4) + 18) * knockback_scaling) + knock_back) * r



1 + ((p - 35 )(115)0.1)


marshal_dash_frames = []
for i in range (1,11):
    image = pygame.image.load(f'assets\sprites\Marshall_Animations\Marshall_dash/Marshal_dash{i}.png').convert_alpha()
    marshal_dash_frames.append(image)

marshal_airidle = []
for i in range(1,32):
    image = pygame.image.load(f'assets\sprites\Marshall_Animations\Marshall_AirIdle/Marshal_Airidle{i}.png').convert_alpha()
    marshal_airidle.append(image)

marshal = Character( 31 , 1.8 , 95, 3, 4, 6  ) # we will probably create character objects in the game class, so this is not needed here  
    

# this should go in the moveset.py file so as to not clutter this character class, which is already going to be big enough 
# hitbox [[length, width, (x relative to player, y relative to player)], [second hitbox stats] ]
character_hitbox = for i in character_moveset[current_move][hitbox]:
    pygame.Rect(character_moveset[current_move]['hitbox'])

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
f_tilt = character_moveset(12, 200, 60, 1.25, 0, '''blank for now''', 7, 22 )
down_tilt = character_moveset(5, 10, 80, 0.2, 0, '''blank for now''', 4, 12, )
up_tilt = character_moveset(8.5, 75, 10, 0.6, 0, '''blank for now''', 6, 15) 
nair = character_moveset(9.5, 90, 45, 1, 0, '''blank for now''', 5, 20)
fair = character_moveset(10, 200, 75, 1.1, 0, '''blank for now''', 8, 20 )
up_air = character_moveset(10, 100, -10, 1, 0, '''blank for now''', 8, 16)
bair = character_moveset(15, 75, 300, 1.4, 0, '''blank for now''', 14, 24)
dair = character_moveset(12, 100, 175, 0.75, 0, '''blank for now''', 15, 25)

#old moveset, changed the moves into a class and defines a few of their stats
'''marshals_moves = {'f_tilt': {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'jab1' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': },
                     'jab2' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': },
                     'rappid_jab' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'up_tilt': {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': },
                     'down_tilt' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': },
                     'dash_attack' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'nair' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'fair' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'bair' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'dair' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'up_air' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'f_smash' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'up_smash' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'down_smash' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'neutral_b' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : ,'invincibility' : , 'hitbox' :  , 'startup': , 'endlag': }, 
                     'up_b' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': },
                     'down_b' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'side_b' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'grab' : {'damage' :0  , 'knock_back' :0 '', 'launch_angle': 0 , 'knockback_scaling' :0 , 'invincibility' : ,'hitbox' :  , 'startup' : , 'endlag': }, 
                     'up_throw' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'down_throw' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'back_throw' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'forward_throw' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'attack_getup' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'ledge_attack' : {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
                     'airddoge' : {'damage' : 0, 'knock_back' :0 '', 'launch_angle': 0 , 'knockback_scaling' :0 , 'invincibility' : (3, 30),'hitbox' :  , 'startup' : 3, 'endlag': 49} }'''
