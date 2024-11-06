import pygame
from time import sleep

class Ammo():
    def __init__(self, bullet_amount = 5, bullet_max = 5):
        self.bullet_amount = bullet_amount
        self.bullet_max = bullet_max
        self.reload_time = 1000
        self.tmp1_time = 0
        self.tmp2_time = 0
        self.sum_time = 0
    
    def update(self):
        self.tmp1_time = pygame.time.get_ticks()
        if self.bullet_amount < self.bullet_max:
            delay_time = self.tmp1_time - self.tmp2_time
            self.sum_time += delay_time
            if self.sum_time >= self.reload_time:
                self.bullet_amount += 1
                self.sum_time = 0
        elif self.bullet_amount == self.bullet_max:
            self.sum_time = 0
        self.tmp2_time = pygame.time.get_ticks()
            
            
# pygame.init()
# clock = pygame.time.Clock()
# ammo = Ammo(bullet_max=5, bullet_amount=1)
# for i in range(150):
#     ammo.update()
#     print(ammo.bullet_amount)
#     clock.tick(50)
    
    

