import pygame
from pygame.sprite import Sprite

# 外星人類別
class Alien(Sprite):
    def __init__(self, screen, ai_settings):
        # 繼承Sprite的初始化
        super().__init__()
        # 讀取視窗、設置物件
        self.screen = screen
        self.ai_settings = ai_settings
        # 讀取外星人的圖檔
        self.image = pygame.image.load("images/alien.png")
        # 縮放外星人的圖檔
        self.image = pygame.transform.scale_by(self.image, 0.1)
        # 將外星人的左上角定位於距離視窗左上角一個外星人的寬度、高度
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 將坐標參數轉化為浮點數
        self.x = float(self.rect.x)
        
    def blit_me(self):
        # 在視窗上畫出外星人
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        # 依據設置的外星人速度更新精確位置
        self.x += self.ai_settings.alien_speed_factor*self.ai_settings.alien_direction
        # 將精確位置輸入實際位置
        self.rect.x = self.x
        
    def check_edge(self):
        # 擷取視窗的長方形
        screen_rect = self.screen.get_rect()
        # 確認自身的長方形左邊是否小於等於0
        if self.rect.left <= 0:
            return True
        # 確認自身的長方形右邊是否超出視窗右側
        elif self.rect.right >= screen_rect.right:
            return True
        
        
        
    