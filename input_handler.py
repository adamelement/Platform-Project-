class InputHandler():

    def jump():
        global air_bound
        if not air_bound:
            character.jump()
            air_bound = True
            double_jump = False
        elif air_bound and not double_jump:
            character.jump()

    def attack():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
        elif keys[pygame.K_LEFT]:
        elif keys[pygame.K_UP]:
        elif keys[pygame.K_DOWN]:      
        else:


    def special_attack():
        if keys[pygame.K_RIGHT]:
        elif keys[pygame.K_LEFT]:
        elif keys[pygame.K_UP]:
        elif keys[pygame.K_DOWN]:      
        else:

    def movement():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:

        elif keys[pygame.K_LEFT]:
        

    def shielding():
        if keys[pygame.K_RIGHT]:
        elif keys[pygame.K_LEFT]:
        elif keys[pygame.K_UP]:
        elif keys[pygame.K_DOWN]:      
        else:

    def 
