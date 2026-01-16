import pygame
pygame.init()
class Stage():
    def __init__(self):

        self.stage_top = pygame.Rect(150, 700, 1620, 100)
        self.stage_bottomr = pygame.Rect(0,0,0,0)
        self.stage_bottoml = pygame.Rect(0,0,0,0)

    def ground_collision(self, player):
        if player.vy >= 0:
            prev_bottom = player.rect.bottom  - player.vy
            if player.rect.right > self.stage_top.left and player.rect.left < self.stage_top.right:
                if prev_bottom <= self.stage_top.top and player.rect.bottom >= self.stage_top.top:
                    player.rect.bottom = self.stage_top.top
                    player.vy = 0
                    player.airborn = False
                    return
        player.airborn = True

    def stage_draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.stage_top)

    def deathbox(self, player):
        if player.y < 900 and player.lives > 0:
            player.lives -= 1
            player.x = 960
            player.y = 800
        elif player.lives < 0:
            return
        



    def stage_collision(self):
        if self.stage_bottomr.colliderect(self.player1.rect):
            self.player1.x += 1
        if self.stage_bottoml.colliderect(self.player1.rect):
            self.player1.x -= 1
        if self.stage_bottomr.colliderect(self.player2.rect):
            self.player2.x += 1
        if self.stage_bottoml.colliderect(self.player2.rect):
            self.player2.x -= 1
    

   