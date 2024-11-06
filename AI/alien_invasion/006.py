import pygame
from pygame.sprite import Sprite 

# 繼承自pygame.sprite裡的Sprite類別
class Laser(Sprite):
    def __init__(self, screen, ship, ai_settings):
        # 沿用Sprite的__init__功能
        super().__init__()
        # 讀取視窗、飛船
        self.screen = screen
        self.ship = ship
        self.color = (255,0,0)
        # 
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 0)
        # 將子彈長方形的座標設置到飛船的正上方
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top
        self.energy = 1000
        self.energy_max = 1000
        self.laser_on = False
        
    def update(self):
        self.rect.centerx = self.ship.rect.centerx
        if laser_on:
            self.energy -= 10
            self.rect.height = self.ship.rect.top
            self.rect.top = 0
        else:
            if energy < energy_max:
                self.energy += 1
            self.rect.height = 0
            self.rect.top = self.ship.rect.top
    def draw_laser(self):
        # 在視窗(self.screen)上面畫出顏色為self.color的長方形(self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    
        
        