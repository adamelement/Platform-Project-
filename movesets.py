


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
marshals_moves = {'f_tilt': {'damage' :  , 'knock_back' : '', 'launch_angle': , 'knockback_scaling' : , 'invincibility' : ,'hitbox' :  , 'startup': , 'endlag': }, 
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
                     'airddoge' : {'damage' : 0, 'knock_back' :0 '', 'launch_angle': 0 , 'knockback_scaling' :0 , 'invincibility' : (3, 30),'hitbox' :  , 'startup' : 3, 'endlag': 49} }
