import pygame
from pygame.sprite import Sprite 

# 繼承自pygame.sprite裡的Sprite類別
class Bullet(Sprite):
    def __init__(self, screen, ship, ai_settings):
        # 沿用Sprite的__init__功能
        super().__init__()
        # 讀取視窗、飛船、設置裡的子彈速度、子彈顏色
        self.screen = screen
        self.ship = ship
        self.speed_factor = ai_settings.bullet_speed_factor
        self.color = ai_settings.bullet_color
        # 根據設置裡的子彈寬度、子彈高度來產生長方形的物件
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # 將子彈長方形的座標設置到飛船的正上方
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 設置浮點數用於更新位置
        self.y = float(self.rect.top)
    def update(self):
        # 更新子彈的精確位置(浮點數)，每次更新都減少speed_factor
        self.y -= self.speed_factor
        # 將子彈的精確位置輸出到實際位置
        self.rect.top = self.y
    def draw_bullet(self):
        # 在視窗(self.screen)上面畫出顏色為self.color的長方形(self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    
        
        