class InputHandler():

    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2



    



    def read(self): 

        keys = pygame.key.get_pressed()
        pressed count = sum(keys)
        if keys[pygame.K_LEFT] and keys == 1: #makes sure that moving is the only input being performed
            character.moving_left()
        if keys[pygame.K_RIGHT] and keys == 1: 
            character.moving_right()

        if keys[pygame.K_SPACE]:
            global airborn
            if not airborn:
                self.character1.jump()
                airborn = True
                double_jump = False
            elif airborn and not double_jump:
                self.character1.jump()
                double_jump = True

        if keys[pygame.K_z]:
            if not airborn:
                if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                    self.character1.f_tilt()
                elif keys[pygame.K_UP]:
                    self.character1.up_tilt()
                elif keys[pygame.K_DOWN]: 
                    self.character1.down_tilt()     
                else:
                    self.character1.jab()

            if airborn:
                if keys[pygame.K_RIGHT]:
                    if character_dirrection == right:
                        self.character1.fair()
                    if character_dirrection == left:
                        self.character1.bair()
                elif keys[pygame.K_LEFT]:
                    if character_dirrection == left:
                        self.character1.fair()
                    if character_dirrection == right:
                        self.character1.bair()
                elif keys[pygame.K_UP]:
                    self.character1.up_air()
                elif keys[pygame.K_DOWN]:  
                    self.character1.down_air()    
                else:
                    self.character1.nair()

        if keys[pygame.K_x]:
            if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                self.character1.f_smash()
            elif keys[pygame.K_UP]:
                self.character1.up_smash()
            elif keys[pygame.K_DOWN]:   
                self.character1.down_smash()   

        if keys[pygame.K_c]:
            if keys[pygame.K_RIGHT]:
                self.character1.forward_special()
            elif keys[pygame.K_UP]:
                self.character1.up_special()
            elif keys[pygame.K_DOWN]:   
                self.character1.down_special()   
            else:
                self.character1.neutral_special()

        if keys[pygame.K_LSHIFT]:
            if airborn:
                self.character1.airdodge()

            if not airborn: 
                self.character1.shield()
                
                if keys[pygame.K_RIGHT]:
                    if character_dirrection == right:
                        self.character1.f_roll()
                    if character_dirrection == left:
                        self.character1.r_roll()
                elif keys[pygame.K_LEFT]:
                    if character_dirrection == right:
                        self.character1.b_roll()
                    if character_dirrection == left:
                        self.character1.f_roll()
                elif keys[pygame.K_DOWN]:
                    self.character1.spotdodge()
                elif keys[pygame.K_z]:
                    self.character1.grab()

        if keys[pygame.K_LCRTL]:
            if not airborn:
                self.character1.grab()

    

    pygame.joystick.init()
    controller = pygame.joystick.Joystick(0) # defines the controller
    controller.init() # initializes the controller
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            
            if event.button == 0: #all different buttons have different names that are numbered, i could explain them at school but i'm just working off the list i have
                    global char2_airborn #made a seperate airborne because as far as i know they aren't different throughout the code. I could very well be missunderstanding or forgetting something though
                    if not char2_airborn:
                        self.character2.jump()
                        char2_airborn = True
                        char2_double_jump = False
                    elif char2_airborn and not char2_double_jump:
                        self.character2.jump()
                        double_jump = True
            if joystick:
                


                    
                    if not char2_airborn:
                        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                            self.character1.f_tilt()
                        elif keys[pygame.K_UP]:
                            self.character1.up_tilt()
                        elif keys[pygame.K_DOWN]: 
                            self.character1.down_tilt()     
                        else:
                            self.character1.jab()
        
                    if airborn:
                        if keys[pygame.K_RIGHT]:
                            if character_dirrection == right:
                                self.character1.fair()
                            if character_dirrection == left:
                                self.character1.bair()
                        elif keys[pygame.K_LEFT]:
                            if character_dirrection == left:
                                self.character1.fair()
                            if character_dirrection == right:
                                self.character1.bair()
                        elif keys[pygame.K_UP]:
                            self.character1.up_air()
                        elif keys[pygame.K_DOWN]:  
                            self.character1.down_air()    
                        else:
                            self.character1.nair()
        
                if keys[pygame.K_x]:
                    if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                        self.character1.f_smash()
                    elif keys[pygame.K_UP]:
                        self.character1.up_smash()
                    elif keys[pygame.K_DOWN]:   
                        self.character1.down_smash()   
        
                if keys[pygame.K_c]:
                    if keys[pygame.K_RIGHT]:
                        self.character1.forward_special()
                    elif keys[pygame.K_UP]:
                        self.character1.up_special()
                    elif keys[pygame.K_DOWN]:   
                        self.character1.down_special()   
                    else:
                        self.character1.neutral_special()
        
                if keys[pygame.K_LSHIFT]:
                    if airborn:
                        self.character1.airdodge()
        
                    if not airborn: 
                        self.character1.shield()
                        
                        if keys[pygame.K_RIGHT]:
                            if character_dirrection == right:
                                self.character1.f_roll()
                            if character_dirrection == left:
                                self.character1.r_roll()
                        elif keys[pygame.K_LEFT]:
                            if character_dirrection == right:
                                self.character1.b_roll()
                            if character_dirrection == left:
                                self.character1.f_roll()
                        elif keys[pygame.K_DOWN]:
                            self.character1.spotdodge()
                        elif keys[pygame.K_z]:
                            self.character1.grab()
        
                if keys[pygame.K_LCRTL]:
                    if not airborn:
                        self.character1.grab()
        
    
