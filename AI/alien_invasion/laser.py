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
        # 設定顏色為紅色
        self.color = (255,0,0)
        # 設定長方形物件，寬度為設置裡的雷射寬度
        self.rect = pygame.Rect(0, 0, ai_settings.laser_width, 0)
        # 將雷射長方形的底部設置到飛船的正上方
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top
        # 設定雷射的能量
        self.energy = 1000
        # 設定雷射能量的上限
        self.energy_max = 1000
        # 設定雷射開關
        self.laser_on = False
        
    def update(self):
        # 更新雷射的水平位置到飛船的水平位置
        self.rect.centerx = self.ship.rect.centerx
        # 若雷射開關打開且能量大於等於10
        if self.laser_on and self.energy >= 10:
            # 能量減少10
            self.energy -= 10
            # 雷射長方形的高度就變成視窗上方到飛船上方
            self.rect.height = self.ship.rect.top
            # 設定雷射長方形的上方在視窗上方
            self.rect.top = 0
        else:
            # 若雷射能量小於最大值
            if self.energy < self.energy_max:
                # 雷射能量加一
                self.energy += 1
            # 將雷射高度設成零
            self.rect.height = 0
            # 將雷射的位置放再飛船上方
            self.rect.top = self.ship.rect.top
    def draw_laser(self):
        # 在視窗(self.screen)上面畫出顏色為self.color的長方形(self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    
        
        