import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, screen, ai_settings):
        super().__init__()
        # 讀取視窗物件
        self.screen = screen
        # 讀取設置物件
        self.ai_settings = ai_settings
        # 讀取飛船的圖像檔
        self.image = pygame.image.load("images/ship.png")
        #self.image = pygame.Surface((50, 50))
        #self.image.fill((255, 0, 0))
        # 縮放飛船的圖像大小,0.1是縮放的倍率
        self.image = pygame.transform.scale_by(self.image, 0.1)
        # 抓取飛船圖像對應的長方形
        self.rect = self.image.get_rect()
        # 抓取視窗對應的長方形
        self.screen_rect = self.screen.get_rect()
        # 飛船水平中心等於視窗水平中心
        self.rect.centerx = self.screen_rect.centerx
        # 飛船底部等於視窗底部
        self.rect.bottom = self.screen_rect.bottom
        # 初始化移動標誌，處理上下左右移動
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        # 精確座標
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
    def blitme(self):
        # 在視窗上繪製飛船
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        # 根據移動標誌來更改飛船的水平位置
        # 判斷是否碰到視窗的右側
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
            # 將精確座標帶入實際座標
            self.rect.centerx = self.centerx
        # 判斷是否碰到視窗的左側
        if self.moving_left and self.rect.left >= 0:
            self.centerx -= self.ai_settings.ship_speed_factor
            # 將精確座標帶入實際座標
            self.rect.centerx = self.centerx
        # 判斷是否碰到視窗的頂部    
        if self.moving_up and self.rect.top >= 0:
            self.centery -= self.ai_settings.ship_speed_factor
            # 將精確座標帶入實際座標
            self.rect.centery = self.centery
        # 判斷是否碰到視窗的底部
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
            # 將精確座標帶入實際座標
            self.rect.centery = self.centery
    # 重置飛船位置
    def reset_ship(self):
        # 飛船水平中心等於視窗水平中心
        self.rect.centerx = self.screen_rect.centerx
        # 飛船底部等於視窗底部
        self.rect.bottom = self.screen_rect.bottom
        # 重置飛船實際位置
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        
        