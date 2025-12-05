class InputHandler():

    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2


    """docstring on class"""

    # have an __init__() method where you pass in an instance of the character class so that you can reference its methods in the read() method 

    
    """Consider having a general read() method checking the keys pressed once and then calling the appropriate method. For example:
   
    def read(self):
    
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_LEFT]:
            #call appropriate methof from character class - character.moving_left() method, maybe
        if keys[pygame.K_RIGHT]:
            # call character.moving_right() for example, from character class
            .
            .
            .

    If there's a controller too, read can be changed to just detect whether there's a controller, in which case it will call a read_controller method, otherwise it will call a read_keyboard method which is the read() method above

    
        
    """

    

    def read(): 

        keys = pygame.key.get_pressed

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
                    self.character1.fair()
                elif keys[pygame.K_LEFT]:
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
                self.character1.dodge()

            if not airborn: 
                self.character1.shield()
                
                if keys[pygame.K_RIGHT]:
                    self.character1.dodge()
                elif keys[pygame.K_LEFT]:
                    self.character1.dodge()
                elif keys[pygame.K_UP]:
                    self.character1.dodge()
                elif keys[pygame.K_DOWN]:
                    self.character1.dodge()
                elif keys[pygame.K_z]:
                    self.character1.grab()

        if keys[pygame.K_LCRTL]:
            if not airborn:
                self.character1.grab()

