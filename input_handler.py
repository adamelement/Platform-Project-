import pygame

class InputHandler():

    def __init__(self):
        self.player1 = player1



    
# 


    def read(self): 

        keys = pygame.key.get_pressed()
        pressed_count = sum(keys)
        if keys[pygame.K_a] and pressed_count == 1: #makes sure that moving is the only input being performed
            self.player1.moving_left()
        if keys[pygame.K_d] and pressed_count == 1: 
            self.player1.moving_right()

        if keys[pygame.K_q]:
            global airborn
            if not airborn:
                self.player1.jump()
                airborn = True
                double_jump = False
            elif airborn and not double_jump:
                self.player1.jump()
                double_jump = True

        if keys[pygame.K_z]:
            if not airborn:
                if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                    attack = 'f_tilt'
                elif keys[pygame.K_w]:
                    attack = 'up_tilt'
                elif keys[pygame.K_s]: 
                    attack = 'down_tilt' 
                else:
                    attack = 'jab'

            if airborn:
                if keys[pygame.K_d]:
                    if character_dirrection == right:
                        attack = 'fair'
                    if character_dirrection == left:
                        attack = 'bair'
                elif keys[pygame.K_a]:
                    if character_dirrection == left:
                        attack = 'fair'
                    if character_dirrection == right:
                        attack = 'bair'
                elif keys[pygame.K_w]:
                    attack = 'up_air'
                elif keys[pygame.K_s]:  
                    attack = 'down_air' 
                else:
                    attack = 'nair'

        if keys[pygame.K_x]:
            if keys[pygame.K_d] or keys[pygame.K_a]:
                attack = 'f_smash'
            elif keys[pygame.K_w]:
                attack = 'up_smash'
            elif keys[pygame.K_s]:   
                attack = 'down_smash'

        if keys[pygame.K_c]:
            if keys[pygame.K_d]:
                attack = 'side_b'
            elif keys[pygame.K_w]:
                attack = 'up_b'
            elif keys[pygame.K_s]:   
                attack = 'down_b'
            else:
                attack = 'neutral_b'

            """Sullivan in case you're working on this file - I sent this and it probably applies to you too:

    Yeah right now the input handler is detecting input and then deciding which specific character method to call. 
    On Friday we talked about simplifying this - maybe just having one attack method that is called with 
    different arguments passed in based on the keys pressed.  That would be a cleaner design. 
    So for example. rather than what you see above, we'd do the following:

    if keys[pygame.K_c]:
    if keys[pygame.K_RIGHT]:
        attack_id = "forward_special"   # must correspond to a key from the moveset dictionary  
    elif keys[pygame.K_UP]:
        attack_id = "up_special"
    elif keys[pygame.K_DOWN]:
        attack_id = "down_special"
    else:
        attack_id = "neutral_s"

    self.player1.attack(attack_id)  

This argument MUST have the same name as the attack key from the moveset dictionary.  If you want the character to be locked in certain moments, 
so unable to make attacks based on things, then maybe this method should be called try_attack(), which then checks whether an attack can take place and if so calls the actual attack method 
all that logic should be in the character class, and there's a variety of ways to go about it. 
I'll let you, Sullivan, and the programmer in game design come up with that - it's a good challenge. 
Let me know what approach you all decide to take for that, and if there are any struggles or questions along the way.  

"""

        if keys[pygame.K_LSHIFT]:
            if airborn:
                self.player1.airdodge()

            if not airborn: 
                self.player1.shield()
                
                if keys[pygame.K_d]:
                    if character_dirrection == right:
                        self.player1.f_roll()
                    if character_dirrection == left:
                        self.player1.r_roll()
                elif keys[pygame.K_a]:
                    if character_dirrection == right:
                        self.player1.b_roll()
                    if character_dirrection == left:
                        self.player1.f_roll()
                elif keys[pygame.K_s]:
                    self.player1.spotdodge()
                elif keys[pygame.K_z]:
                    attack = 'grab'
                    self.player1.attack(attack)

        if keys[pygame.K_LCRTL]:
            if not airborn:
                attack = 'grab'



        if keys[pygame.K_j] and keys == 1: #makes sure that moving is the only input being performed
            self.player2.moving_left()
        if keys[pygame.K_l] and keys == 1: 
            self.player2.moving_right()

        if keys[pygame.K_u]:
            global airborn
            if not airborn:
                self.player2.jump()
                airborn = True
                double_jump = False
            elif airborn and not double_jump:
                self.player2.jump()
                double_jump = True

        if keys[pygame.K_m]:
            if not airborn:
                if keys[pygame.K_l] or keys[pygame.K_j]:
                    attack = 'f_tilt'
                    self.player2.attack(attack)
                elif keys[pygame.K_i]:
                    attack = 'up_tilt'
                    self.player2.attack(attack)
                elif keys[pygame.K_k]: 
                    attack = 'down_tilt' 
                    self.player2.attack(attack)  
                else:
                    attack = 'jab'
                    self.player2.attack(attack)

            if airborn:
                if keys[pygame.K_l]:
                    if character_dirrection == right:
                        attack = 'fair'
                        self.player2.attack(attack)
                    if character_dirrection == left:
                        attack = 'bair'
                        self.player2.attack(attack)
                elif keys[pygame.K_j]:
                    if character_dirrection == left:
                        attack = 'fair'
                        self.player2.attack(attack)
                    if character_dirrection == right:
                        attack = 'bair'
                        self.player2.attack(attack)
                elif keys[pygame.K_i]:
                    attack = 'up_air'
                    self.player2.attack(attack)
                elif keys[pygame.K_k]:  
                    attack = 'down_air' 
                    self.player2.attack(attack) 
                else:
                    attack = 'nair'
                    self.player2.attack(attack)

        if keys[pygame.K_COMMA]:
            if keys[pygame.K_l] or keys[pygame.K_j]:
                attack = 'f_smash'
                self.player2.attack(attack)
            elif keys[pygame.K_i]:
                attack = 'up_smash'
                self.player2.attack(attack)
            elif keys[pygame.K_k]:   
                attack = 'down_smash'
                self.player2.attack(attack)

        if keys[pygame.K_PERIOD]:
            if keys[pygame.K_l]:
                attack = 'side_b'
                self.player2.attack(attack)
            elif keys[pygame.K_i]:
                attack = 'up_b'
                self.player2.attack(attack)
            elif keys[pygame.K_k]:   
                attack = 'down_b'
                self.player2.attack(attack)
            else:
                attack = 'neutral_b'
                self.player2.attack(attack)
        
        if keys[pygame.K_n]:
            if airborn:
                self.player2.airdodge()

            if not airborn: 
                self.player2.shield()
                
                if keys[pygame.K_l]:
                    if character_direction == right:
                        self.player2.f_roll()
                    if character_direction == left:
                        self.player2.r_roll()
                elif keys[pygame.K_j]:
                    if character_direction == right:
                        self.player2.b_roll()
                    if character_direction == left:
                        self.player2.f_roll()
                elif keys[pygame.K_k]:
                    self.player2.spotdodge()
                elif keys[pygame.K_m]:
                    attack = 'grab'
                    self.player2.attack(attack)
        if keys[pygame.K_SPACE]:
            if not airborn:
                attack = 'grab'



    

    pygame.joystick.init()
    controller = pygame.joystick.Joystick(0) # defines the controller
    controller.init() # initializes the controller
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:

            buttons = pygame.button.get_pressed()
            button_count = sum(buttons)
            axis_x = joystick.get_axis(0)
            axis_y = joystick.get_axis(1)
            deadzone = 0.2 
            
            if axis_x > deadzone and buttons == 0: 
                character.moving_right
            elif axis_x < -deadzone: 
                character.moving_left

                

            
            if event.button == 3: #all different buttons have different names that are numbered, i could explain them at school but i'm just working off the list i have
                    global airborn #made a seperate airborne because as far as i know they aren't different throughout the code. I could very well be missunderstanding or forgetting something though
                    if not airborn:
                        self.character.jump()
                        airborn = True
                        char2_double_jump = False
                    elif airborn and not char2_double_jump:
                        self.character.jump()
                        char2_double_jump = True
            if event.button == 2:
                if not airborn:
                    if axis_x > 0.2 or axis_x < -0.2:
                        attack = 'f_tilt'
                    if axis_y < 0.2:
                        attack = 'up_tilt'
                    if axis_y > -0.2:
                        attack = 'down_tilt'
                else:
                        self.player2.jab()

            if airborn:
                if axis_x > deadzone:
                    if player2_dirrection == right:
                        attack = 'fair'
                    if player2_dirrection == left:
                        attack = 'bair'
                elif axis_x < deadzone:
                    if player2_dirrection == left:
                        attack = 'fair'
                    if player2_dirrection == right:
                        attack = 'bair'
                elif axis_y > deadzone:
                    attack = 'up_air'
                elif axis_y < deadzone:  
                    attack = 'down_air'
                else:
                    attack = 'nair'
                    
            if event.button == 1: 
                if axis_x > deadzone or axis_x < -deadzone:
                    attack = 'f_smash'
                elif axis_y > deadzone:
                    attack = 'up_smash'
                elif axis_y < -deadzone:
                    attack = 'down_smash'
            if event.button == 0:
                if axis_x > deadzone or axis_y < -deadzone:
                    attack = 'side_b'
                elif axis_y > deadzone:
                    attack = 'up_b'
                elif axis_y < -deadzone:   
                    attack = 'down_b'
                else:
                    attack = 'neutral_b'
            if event.button == 5:
                if airborn:
                    self.character.airdodge()
                if airborn:
                    self.character.shield()
                if axis_x > deadzone:
                    if facing_right:
                        self.character.f_roll()
                    if not facing_right:
                        self.character.b_roll()
                elif axis_x < -deadzone:
                    if facing_right:
                        self.character.b_roll()
                    if not facing_right:
                        self.character.f_roll()
                elif axis_y < -deadzone:
                    self.character.spotdodge()
                elif event.button == 3:
                    attack = 'grab'
            if event.button == 5:
                if not airborn:
                    attack = 'grab'
                
        
    
