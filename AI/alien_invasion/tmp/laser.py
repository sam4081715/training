import pygame
from pygame.sprite import Sprite 

# 繼承自pygame.sprite裡的Sprite類別
class Laser(Sprite):
    def __init__(self, screen, ship, ai_settings):
        # 沿用Sprite的__init__功能
        super().__init__()
        # 讀取視窗、飛船、設置裡的子彈速度、子彈顏色
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ship = ship
        self.color = (255,0,0)
        # 根據設置裡的子彈寬度、子彈高度來產生長方形的物件
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 1)
        # 將子彈長方形的座標設置到飛船的正上方
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top
        # 設置浮點數用於更新位置
        self.laser_on = False
        self.energy = 1000
    def update(self):
        # 更新子彈的精確位置(浮點數)，每次更新都減少speed_factor
        self.rect.centerx = self.ship.rect.centerx
        # 將子彈的精確位置輸出到實際位置
        if laser_on:
            self.rect.top = self.screen_rect.top
            self.energy -= 10
        else:
            self.rect.top = ship.rect.top+1
            self.energy += 10
    def draw_bullet(self):
        # 在視窗(self.screen)上面畫出顏色為self.color的長方形(self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    
        
        