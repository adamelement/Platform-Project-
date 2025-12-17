import pygame

attack = ''
class InputHandler():

    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2



    
# 


    def read_keyboard(self): 

        keys = pygame.key.get_pressed()
        pressed_count = sum(keys)
        if keys[pygame.K_a] or keys[pygame.K_LEFT] and pressed_count == 1: #makes sure that moving is the only input being performed
            self.character1.moving_left()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]  and pressed_count == 1: 
            self.character1.moving_right()

        if keys[pygame.K_q]:
            if not self.character1.airborn:
                self.character1.jump()
                self.character1.airborn = True
                double_jump = False
            elif self.character1.airborn and not double_jump:
                self.character1.jump()
                double_jump = True

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

    self.character1.attack(attack_id)  

This argument MUST have the same name as the attack key from the moveset dictionary.  If you want the character to be locked in certain moments, 
so unable to make attacks based on things, then maybe this method should be called try_attack(), which then checks whether an attack can take place and if so calls the actual attack method 
all that logic should be in the character class, and there's a variety of ways to go about it. 
I'll let you, Sullivan, and the programmer in game design come up with that - it's a good challenge. 
Let me know what approach you all decide to take for that, and if there are any struggles or questions along the way.  

"""

        if keys[pygame.K_LSHIFT]:
            if self.character1.airborn:
                self.character1.airdodge()

            if not self.character1.airborn: 
                self.character1.shield()
        
                
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    if self.character1.facing_right:
                        self.character1.f_roll()
                    if not self.character1.facing_right:
                        self.character1.r_roll()
                elif keys[pygame.K_a or keys[pygame.K_LEFT]]:
                    if self.character1.facing_right:
                        self.character1.b_roll()
                    if not self.character1.facing_right:
                        self.character1.f_roll()
                elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    self.character1.spotdodge()
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
            elif self.character1.airborn:
                attack = 'idle'
            self.character1.animation(attack)
            attack = ''




        if keys[pygame.K_j] and keys == 1: #makes sure that moving is the only input being performed
            self.character2.moving_left()
        if keys[pygame.K_l] and keys == 1: 
            self.character2.moving_right()

        if keys[pygame.K_u]:
            if not self.character2.airborn:
                self.character2.jump()
                self.character2.airborn = True
                double_jump = False
            elif self.character2.airborn and not double_jump:
                self.character2.jump()
                double_jump = True

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
                self.character2.airdodge()

            if not self.character2.airborn: 
                self.character2.shield()
                
                if keys[pygame.K_l]:
                    if self.character2.facing_right:
                        self.character2.f_roll()
                    if not self.character2.facing_right:
                        self.character2.r_roll()
                elif keys[pygame.K_j]:
                    if self.character2.facing_right:
                        self.character2.b_roll()
                    if not self.character2.facing_right:
                        self.character2.f_roll()
                elif keys[pygame.K_k]:
                    self.character2.spotdodge()
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
            elif self.character2.airborn:
                attack = 'idle'
            self.character2.animation(attack)
            attack = ''



    
    def controller_read(self):
        pygame.joystick.init()
        if pygame.joystick.get_count() != 0:
            controller = pygame.joystick.Joystick(0) # defines the controller
            controller.init() # initializes the controller

            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
    
                    buttons = [controller.get_button(i) for i in range(controller.get_numbuttons())]
                    button_count = sum(buttons)
                    axis_x = controller.get_axis(0)
                    axis_y = controller.get_axis(1)
                    deadzone = 0.2 
                    
                    if axis_x > deadzone and buttons == 0: 
                        self.character.moving_right
                    elif axis_x < -deadzone: 
                        self.character.moving_left
    
                        
    
                    
                    if event.button == 3: #all different buttons have different names that are numbered, i could explain them at school but i'm just working off the list i have
                            if not self.character2.airborn: #made a seperate airborne because as far as i know they aren't different throughout the code. I could very well be missunderstanding or forgetting something though
                                self.character.jump()
                                self.character2.airborn = True
                                char2_double_jump = False
                            elif self.character2.airborn and not char2_double_jump:
                                self.character.jump()
                                char2_double_jump = True
                    if event.button == 2:
                        if not self.character2.airborn:
                            if axis_x > deadzone or axis_x < -deadzone:
                                attack = 'f_tilt'
                            if axis_y > deadzone:
                                attack = 'up_tilt'
                            if axis_y < -deadzone:
                                attack = 'down_tilt'
                        else:
                                self.character2.jab()
    
                    if self.character2.airborn:
                        if axis_x > deadzone:
                            if self.character2.facing_right:
                                attack = 'fair'
                            if not self.character2.facing_right:
                                attack = 'bair'
                        elif axis_x < -deadzone:
                            if not self.character2.facing_right:
                                attack = 'fair'
                            if self.character2.facing_right:
                                attack = 'bair'
                        elif axis_y > deadzone:
                            attack = 'up_air'
                        elif axis_y < -deadzone:  
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
                    if event.button == 4:
                        if self.character2.airborn:
                            self.character.airdodge()
                        if not self.character2.airborn:
                            self.character.shield()
                        if axis_x > deadzone:
                            if self.character2.facing_right:
                                self.character.f_roll()
                            if not self.character2.facing_right:
                                self.character.b_roll()
                        elif axis_x < -deadzone:
                            if not self.character2.facing_right:
                                self.character.b_roll()
                            if self.character2.facing_right:
                                self.character.f_roll()
                        elif axis_y < -deadzone:
                            self.character.spotdodge()
                        elif event.button == 3:
                            attack = 'grab'
                    if event.button == 4:
                        if not self.character2.airborn:
                            attack = 'grab'
        if len(attack) != 0:
            self.character2.attack(attack)
            self.character2.animation(attack)
            attack = ''
        else:
            if self.character2.airborn:
                attack = 'airidle'
            elif self.character2.airborn:
                attack = 'idle'
            self.character2.animation(attack)
            attack = ''
                    
                    
            
        
