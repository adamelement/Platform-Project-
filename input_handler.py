class InputHandler():

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

    
class InputHandler:

    def read(): 

        keys = pygame.key.get_pressed

        if keys[pygame.K_SPACE]:
            global air_bound
            if not air_bound:
                character.jump()
                air_bound = True
                double_jump = False
            elif air_bound and not double_jump:
                character.jump()
                double_jump = True

        if keys[pygame.K_z]:
            if not air_bound:
                if keys[pygame.K_RIGHT]:
                elif keys[pygame.K_LEFT]:
                elif keys[pygame.K_UP]:
                elif keys[pygame.K_DOWN]:      
                else:

            if air_bound:
                if keys[pygame.K_RIGHT]:
                elif keys[pygame.K_LEFT]:
                elif keys[pygame.K_UP]:
                elif keys[pygame.K_DOWN]:      
                else:

        if keys[pygame.K_x]:
            if keys[pygame.K_RIGHT]:
            elif keys[pygame.K_LEFT]:
            elif keys[pygame.K_UP]:
            elif keys[pygame.K_DOWN]:      
            else:

        if keys[pygame.K_c]:
            if keys[pygame.K_RIGHT]:
            elif keys[pygame.K_LEFT]:
            elif keys[pygame.K_UP]:
            elif keys[pygame.K_DOWN]:      
            else:

        if keys[pygame.K_LSHIFT]:
            if air_bound:
                character.dodge()

            if not air_bound: 
                character.shield()
                
                if keys[pygame.K_RIGHT]:
                elif keys[pygame.K_LEFT]:
                elif keys[pygame.K_UP]:
                elif keys[pygame.K_DOWN]:
                elif keys[pygame.K_z]:
                    character.grab()

        if keys[pygame.K_LCRTL]:
            if not air_bound:
                character.grab()

